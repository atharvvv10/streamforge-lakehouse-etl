FROM debian:bullseye-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip python3-dev build-essential libsasl2-dev librdkafka-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /data/app_src

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY producer.py .

CMD ["/usr/bin/python3", "producer.py"]