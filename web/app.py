from asyncpg import create_pool
from sanic import Sanic, response


app = Sanic("DeliveryHero")

APP_HOST = '0.0.0.0'
APP_PORT = 8899
APP_DEBUG_MODE = False
APP_ACCESS_LOG = True
DB_USER = 'postgres'
DB_PASSWORD = 'mypass21!'
DB_HOST = 'db'
DB_PORT = '5432'
DB_NAME = 'postgres'
DB_CONN_POOL_MIN_SIZE = 10
DB_CONN_POOL_MAX_SIZE = 100
DB_CONN_POOL_MAX_QUERIES = 1500
DB_CONN_POOL_CONNECTION_TIMEOUT = 600


@app.route("/api/v1/connections")
async def test(request):
    """
    Function returns the amount of current connection to DB
    """
    pool = request.app.config['pool']
    async with pool.acquire() as conn:
        sql = '''
                SELECT sum(numbackends) FROM pg_stat_database; 
            '''
        sql_result = await conn.fetch(sql)
        return response.json({'connections': {"amount": str(sql_result[0])}}, status=200)


@app.route("/healthz")
async def test(request):
    """
    Function returns health-check probe
    """
    pool = request.app.config['pool']
    async with pool.acquire() as conn:
        sql = '''
                SELECT 1; 
            '''
        sql_result = await conn.fetch(sql)

        if sql_result:
            return response.json({'db_connection': 'Ok', 'alive': True}, status=200)

        else:
            return response.json({'db_connection': 'Failed', 'alive': False}, status=500)


@app.listener('before_server_start')
async def register_db(app, loop):
    """Function creates connection pool for the DB"""

    conn = f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    app.config['pool'] = await create_pool(
                    dsn=conn,
                    min_size=DB_CONN_POOL_MIN_SIZE,
                    max_size=DB_CONN_POOL_MAX_SIZE,
                    max_queries=DB_CONN_POOL_MAX_QUERIES,
                    max_inactive_connection_lifetime=DB_CONN_POOL_CONNECTION_TIMEOUT,
                    loop=loop)


@app.listener('after_server_stop')
async def close_connection(app):
    pool = app.config['pool']
    async with pool.acquire() as conn:
        await conn.close()


if __name__ == "__main__":
    app.run(host=APP_HOST,
            port=APP_PORT,
            access_log=APP_ACCESS_LOG,
            debug=APP_DEBUG_MODE)