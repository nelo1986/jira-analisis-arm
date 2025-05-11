FROM --platform=linux/arm64 python:3.9

ENV SUPERSET_HOME=/app
WORKDIR $SUPERSET_HOME

# Copiar configuración personalizada
COPY superset_config.py /app/
ENV SUPERSET_CONFIG_PATH=/app/superset_config.py

# Instalar dependencias del sistema necesarias para Superset + PostgreSQL
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    libxml2-dev \
    libxslt1-dev \
    libldap2-dev \
    libsasl2-dev \
    git \
    postgresql-client \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Instalar Superset
RUN pip install --upgrade pip && pip install apache-superset psycopg2-binary marshmallow==3.20.1 pillow

# Copiar el script de arranque
COPY run-server.sh /usr/bin/run-server.sh
RUN chmod +x /usr/bin/run-server.sh

ENTRYPOINT ["/usr/bin/run-server.sh"]
