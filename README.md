# web-app
### Task A (Web application)

1. To run the Web-application locally you need to use python3 with version 3.6+ 
2. First install all dependencies using command below:
```apex
python3 -m pip3 install -r ./web/requirements.txt
```
3. Then launch DB (postgreSQL) from docker-compose file:
```apex
docker-compose up -d 
```
4. Finally run the web-application
```apex
python3 ./web/app.py
```
5. Healths check probe available, by default in the path `http://localhost:8899/healthz` 
6. To receive the amount of current connections to DB send GET request to `http://localhost:8899/api/v1/connections`