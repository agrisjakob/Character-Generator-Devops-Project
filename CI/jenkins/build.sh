
sudo docker login --username=$docker_username --password=$docker_password

sudo docker-compose build

sudo docker-compose push
