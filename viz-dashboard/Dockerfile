FROM python:3.9-slim AS builder
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_ROOT_USER_ACTION=ignore
WORKDIR /tmp/packages
RUN pip install --no-cache-dir \
    psycopg2-binary==2.9.9 \
    sqlalchemy-trino==0.4.0
FROM debian:bookworm-slim
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip python3-setuptools ca-certificates openssl curl && \
    rm -rf /var/lib/apt/lists/*
ENV APP_USER=superset
RUN useradd -m ${APP_USER}
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
WORKDIR /usr/local/superset_app
COPY superset_config.py ./app_config.py
COPY ./superset-init.sh /usr/local/bin/start-viz-app.sh
RUN chmod +x /usr/local/bin/start-viz-app.sh
ENV DOCKER_USER=${APP_USER} \
    SUP_CONFIG_FILE_PATH=/usr/local/superset_app/app_config.py \
    ADMIN_USERNAME=$ADMIN_USERNAME \
    ADMIN_EMAIL=$ADMIN_EMAIL \
    ADMIN_PASS=$ADMIN_PASSWORD
ENV SUPERSET_CONFIG_PATH ${SUP_CONFIG_FILE_PATH}
USER ${APP_USER}
CMD [ "/usr/local/bin/start-viz-app.sh" ]