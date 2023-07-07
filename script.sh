docker stop pro-novo-bot-container

docker rm pro-novo-bot-container

docker build -t pro-novo-bot .

docker run -d --name pro-novo-bot-container pro-novo-bot
