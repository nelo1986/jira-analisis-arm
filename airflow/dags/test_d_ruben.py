from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False,
}

with DAG(
    dag_id='test_postgres_dag',
    default_args=default_args,
    schedule_interval=None,  # Se ejecuta solo manualmente
    tags=['test'],
) as dag:

    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres_jira',  # Debe estar definido en Admin > Connections
        sql="""
            CREATE TABLE IF NOT EXISTS test_table (
                id SERIAL PRIMARY KEY,
                message TEXT
            );
        """,
    )

    insert_row = PostgresOperator(
        task_id='insert_row',
        postgres_conn_id='postgres_jira',
        sql="""
            INSERT INTO test_table (message) VALUES ('¡Hola desde Airflow!');
        """,
    )

    create_table >> insert_row
