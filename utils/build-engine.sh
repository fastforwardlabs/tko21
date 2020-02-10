#!/bin/sh

#sudo yum install docker

ENGINE_NAME='engine'
ENGINE_TAG='11-cml1.4-demo'
DOCKER_REPO='cdsw'

sudo docker build --network=host -t $ENGINE_NAME:$ENGINE_TAG . -f Dockerfile

#use the following lines if you want to save and distribute the engine to CDSW servers
#ENGINE_FILE=${ENGINE_NAME}-${ENGINE_TAG}.tar
#sudo docker image save -o ./$ENGINE_FILE $ENGINE_NAME:$ENGINE_TAG
#sudo chmod 755 ./$ENGINE_FILE

#use the following lines to push the engine to the Docker Hub repo.
IMAGE_ID=`sudo docker images | awk -v name="$ENGINE_NAME" -v tag="$ENGINE_TAG" -F" " '$1==name && $2==tag { print $3 }'`
sudo docker tag $IMAGE_ID ${DOCKER_REPO}/${ENGINE_NAME}:${ENGINE_TAG}
sudo docker login
sudo docker push  ${DOCKER_REPO}/${ENGINE_NAME}:${ENGINE_TAG}
