docker stop pro-novo-bot-container

docker rm pro-novo-bot-container

docker build -t pro-novo-bot .

docker run -d  --name pro-novo-bot-container --add-host=database:209.38.224.54


#docker run -d -it -p 5432:5432 -v /var/lib/docker/volumes/pro-novo_volume/_data/mydatabase.db:/home/can/mydatabase.db:ro alpine chown can:can /home/can/mydatabase.db
#
