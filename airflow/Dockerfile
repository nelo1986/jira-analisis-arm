FROM --platform=linux/arm64 python:3.9

ENV AIRFLOW_HOME=/opt/airflow
ENV AIRFLOW__CORE__EXECUTOR=SequentialExecutor

RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    libpq-dev \
    curl \
    && apt-get clean

RUN pip install --upgrade pip && \
    pip install apache-airflow[postgres,celery,redis]==2.8.0 && \
    pip install 'psycopg2-binary<3' && \
    pip install jira[cli] python-dotenv Flask-Session==0.4.0

RUN mkdir -p $AIRFLOW_HOME/dags
WORKDIR $AIRFLOW_HOME

EXPOSE 8080

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN pip install 'WTForms<3.1'
ENTRYPOINT ["/entrypoint.sh"]
