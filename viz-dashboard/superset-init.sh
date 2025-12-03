#!/bin/bash
export SUPERUSER_NAME="${ADMIN_USERNAME}"
export SUPERUSER_EMAIL="${ADMIN_EMAIL}"
export SUPERUSER_PASSWORD="${ADMIN_PASSWORD}"

/usr/local/bin/superset-cli create-user \
    --username "${SUPERUSER_NAME}" \
    --firstname 'Data' \
    --lastname 'Viz' \
    --email "${SUPERUSER_EMAIL}" \
    --password "${SUPERUSER_PASSWORD}" \
    --role 'Admin'

/usr/local/bin/superset-cli db-migrate
/usr/local/bin/superset-cli setup-roles

/usr/bin/python3 /usr/local/superset/bin/gunicorn --workers 4 --bind 0.0.0.0:8088