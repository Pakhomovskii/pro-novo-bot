FROM ubuntu:latest
RUN apt-get -y update
RUN apt-get install -y sqlite3 python python3-pip

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]