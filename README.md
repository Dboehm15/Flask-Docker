# Flask-Valheim-Docker


### Build in docker
docker build -t python-val .
### Run docker
docker run -d -p 80:80 python-val
### Get dockerID
docker ps
### Connect to docker
docker exec -it <dockerID> /bin/sh
### Kill a docker
docker kill <dockerID>