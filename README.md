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

### Task B (Dockerizing the Application)

1. To build the application locally use `docker-compose build`
2. To run application after the build use `docker-compose up`
3. To configure build/launch parameters change `./web/.env`  file


### Task C (Deployment to K8s)

1. To deploy the application in the Kubernetes cluster (v1.19+) provide the necessary parameters to the file `deploy.env` 
Set corresponding values for the: 
   ```apex
     APPLICATION_NAME - name of the application in the docker repository
     APP_VERSION - tag for the docker image
     APP_DNS - DNS name for the ingress which the application will be available outside from K8s cluster 
     DOCKER_PASSWORD - Password for the docker registry
     DOCKER_USER - Username for the docker registry
     DOCKER_REGISTRY - Docker registry name to push the image
     DOCKER_REPOSITORY - Repository name
     RELEASE_NAME - Helm release name
   ```
   
2. Run the bash script `deploy.sh` to deploy the service

#### Some notes:
To simplify the application deployment were made intentional assumptions according stability and durability for the postgres deployment. Was chosen deployment with emptyDir volume type but for the production ready db-service should be used at least Statefulset with external PVC. Also skipped TLS and wild-card certificates configurations.    
Weren't implemented additional logging for the web-application, try/except blocks and monitoring.   
