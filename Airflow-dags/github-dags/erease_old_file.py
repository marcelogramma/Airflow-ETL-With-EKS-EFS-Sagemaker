from datetime import datetime
from pathlib import Path
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


default_args = {"owner": "MG", "retries": 0}

dag = DAG(
    "erease_old_files",
    default_args=default_args,
    schedule_interval="0 5 1 * *",
    start_date=days_ago(1),
)
erease_old_files = BashOperator(
    task_id="erease_old_files", bash_command=" /opt/airflow/data/delete.sh ", dag=dag
)
