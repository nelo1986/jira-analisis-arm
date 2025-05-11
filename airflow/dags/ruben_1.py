from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False,
}

# Generar el SQL con 100 INSERTs
insert_sql = "\n".join(
    [f"INSERT INTO test_table (message) VALUES ('Mensaje número {i}');" for i in range(1, 101)]
)

with DAG(
    dag_id='ruben_postgres_dag',
    default_args=default_args,
    schedule_interval=None,
    tags=['test'],
) as dag:

    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres_jira',
        sql="""
            CREATE TABLE IF NOT EXISTS test_table (
                id SERIAL PRIMARY KEY,
                message TEXT
            );
        """,
    )

    insert_rows = PostgresOperator(
        task_id='insert_100_rows',
        postgres_conn_id='postgres_jira',
        sql=insert_sql,
    )

    create_table >> insert_rows
