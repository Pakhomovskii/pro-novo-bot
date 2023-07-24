FROM ubuntu:latest
RUN apt-get -y update
RUN apt-get install -y sqlite3 python3 python3-pip python-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]