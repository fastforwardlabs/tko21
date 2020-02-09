#!/bin/sh

#sudo yum install docker

ENGINE_NAME='engine'
ENGINE_INSTANCE='11-cml1.4-tko'
ENGINE_FILE=${ENGINE_NAME}-${ENGINE_INSTANCE}.tar

sudo docker build --network=host -t $ENGINE_NAME:$ENGINE_INSTANCE . -f Dockerfile
sudo docker image save -o ./$ENGINE_FILE $ENGINE_NAME:$ENGINE_INSTANCE
sudo chmod 755 ./$ENGINE_FILE
