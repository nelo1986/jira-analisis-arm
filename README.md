# JIRA Analytics Stack (ARM64)

Este proyecto contiene una pila de contenedores para ejecutar **Apache Superset**, **Apache Airflow** y **PostgreSQL** en arquitectura ARM64 (como Raspberry Pi).

## 🚀 Servicios incluidos

- **Superset** (`superset-arm64`): dashboard para análisis de datos.
- **Airflow** (`airflow-arm64`): orquestación de tareas para procesar datos de JIRA.
- **PostgreSQL**: base de datos donde se almacenan los datos extraídos.

## 📦 Requisitos

- Docker + Buildx
- Docker Compose
- Raspberry Pi o sistema ARM64

## 🛠️ Cómo construir las imágenes

```bash
docker buildx build --platform linux/arm64 -t superset-arm64 ./superset
docker buildx build --platform linux/arm64 -t airflow-arm64 ./airflowx
