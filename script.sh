docker stop pro-novo-bot-container

docker rm pro-novo-bot-container

docker build -t pro-novo-bot .

docker run -d -it -p 5432:5432 --protocol=tcp -u root -v pro-novo_volume:/data --name pro-novo-bot-container pro-novo-bot
