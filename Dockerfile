FROM ubuntu:latest
RUN apt-get -y update
RUN apt-get install -y sqlite3 python3 python3-pip

WORKDIR /app

COPY requirements.txt .

RUN sudo pip  pip install install python-dev-tools
RUN sudo pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]