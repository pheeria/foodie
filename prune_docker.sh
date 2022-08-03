docker system prune;
docker stop $(docker ps -a -q);
docker rm $(docker ps -a -q);
docker rmi $(docker images -a -q);
docker volume prune;
docker network prune;
