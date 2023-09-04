docker stop pro-novo-bot-container

docker rm pro-novo-bot-container

docker build -t pro-novo-bot .

docker run -d -it -p 5433:5433 -v pro-novo_volume:/data --name pro-novo-bot-container pro-novo-bot
