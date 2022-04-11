#!/bin/bash
export $(cat deploy.env | xargs)
# Enable debug mode
set -x

# Logging to the docker registry
echo ${DOCKER_PASSWORD} | docker login --username ${DOCKER_USER} --password-stdin ${DOCKER_REGISTRY}
#
## Building and pushing the application to the registry
cd web && docker build -t ${APPLICATION_NAME} .
docker tag ${APPLICATION_NAME} ${DOCKER_REPOSITORY}/${APPLICATION_NAME}:${APP_VERSION}
docker push ${DOCKER_REPOSITORY}/${APPLICATION_NAME}:${APP_VERSION}
#
cd .. && export WEBAPP_IMAGE=${DOCKER_REGISTRY}/${DOCKER_REPOSITORY}/${APPLICATION_NAME}
helm upgrade --install ${RELEASE_NAME} webapp --set "image.repository=${WEBAPP_IMAGE},image.tag=${APP_VERSION},ingress.host=${APP_DNS}" --dry-run