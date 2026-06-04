from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id="customer_etl_pipeline",
    start_date=datetime(2025,1,1),
    schedule="@daily",
    catchup=False
) as dag:

    start = EmptyOperator(
        task_id="start"
    )

    run_spark_job = SparkSubmitOperator(
        task_id="customer_etl",
        application="/opt/spark_jobs/customer_etl.py",
        conn_id="spark_default"
    )

    end = EmptyOperator(
        task_id="end"
    )

    start >> run_spark_job >> end
    
