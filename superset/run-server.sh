#!/bin/bash
export FLASK_APP=superset
export SUPERSET_CONFIG_PATH=/app/superset_config.py

# Inicializar la base de datos si es necesario
superset db upgrade

# Crear usuario admin si no existe
superset fab create-admin \
  --username admin \
  --firstname Superset \
  --lastname Admin \
  --email admin@superset.com \
  --password admin || true

# Inicializar superset
superset init

# Lanzar el servidor
superset run -h 0.0.0.0 -p 8088 --with-threads --reload --debugger
