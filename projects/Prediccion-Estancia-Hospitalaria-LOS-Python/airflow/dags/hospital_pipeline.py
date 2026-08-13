from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025,1,1)
}

with DAG(
    dag_id="hospital_ml_pipeline",
    schedule_interval=None,
    catchup=False,
    default_args=default_args
) as dag:

    upload_hdfs = BashOperator(
        task_id="upload_excel_hdfs",
        bash_command="""
        python /opt/airflow/projects/xlsx_to_hdfs_pipeline.py
        """
    )

    train_model = BashOperator(
        task_id="train_model",
        bash_command="""
        spark-submit /opt/airflow/projects/App.py
        """
    )

    upload_hdfs >> train_model
