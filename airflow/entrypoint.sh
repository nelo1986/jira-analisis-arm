#!/bin/bash
set -e

# Esperar si la DB aún no está lista (opcional si usas depends_on con healthchecks)
sleep 5

# Inicializar la base de datos
airflow db upgrade

# Crear usuario admin (ignora error si ya existe)
airflow users create \
  --username admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com \
  --password admin || true

# Iniciar el scheduler en segundo plano
airflow scheduler &

# Iniciar el servidor web
exec airflow webserver
