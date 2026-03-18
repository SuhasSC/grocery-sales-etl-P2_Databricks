from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta
import requests

# -------------------------------
# CONFIGURATION
# -------------------------------

DATABRICKS_JOB_ID = 829654937308348

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"


# -------------------------------
# SLACK MESSAGE FUNCTION
# -------------------------------

def send_slack_message(message):
    payload = {"text": message}
    requests.post(SLACK_WEBHOOK_URL, json=payload)


# -------------------------------
# FAILURE ALERT
# -------------------------------

def slack_failure_alert(context):

    dag_id = context["dag"].dag_id
    task_id = context["task_instance"].task_id
    execution_date = context["execution_date"]
    log_url = context["task_instance"].log_url

    message = f"""
🚨 Airflow Pipeline Failed

DAG: {dag_id}
Task: {task_id}
Execution Date: {execution_date}

Logs: {log_url}
"""

    send_slack_message(message)


# -------------------------------
# SUCCESS ALERT WITH METRICS
# -------------------------------

def slack_success_alert(context):

    dag_id = context["dag"].dag_id
    task_id = context["task_instance"].task_id
    execution_date = context["execution_date"]

    start_time = context["task_instance"].start_date
    end_time = context["task_instance"].end_date

    runtime = end_time - start_time

    message = f"""
✅ Airflow Pipeline Succeeded

DAG: {dag_id}
Task: {task_id}
Execution Date: {execution_date}

Runtime: {runtime}

Logs: {context['task_instance'].log_url}
"""

    send_slack_message(message)


# -------------------------------
# DEFAULT DAG ARGUMENTS
# -------------------------------

default_args = {
    "owner": "airflow",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


# -------------------------------
# DAG DEFINITION
# -------------------------------

with DAG(
    dag_id="databricks_grocery_sales_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="0 0 * * *",
    catchup=False,
    default_args=default_args,
    on_failure_callback=slack_failure_alert,
    tags=["databricks", "grocery_pipeline"],
) as dag:

    start_pipeline = EmptyOperator(
        task_id="start_pipeline"
    )

    run_databricks_job = DatabricksRunNowOperator(
        task_id="run_databricks_job",
        databricks_conn_id="databricks_default",
        job_id=DATABRICKS_JOB_ID,
        execution_timeout=timedelta(minutes=30),
        on_success_callback=slack_success_alert
    )

    data_quality_check = EmptyOperator(
        task_id="data_quality_check"
    )

    end_pipeline = EmptyOperator(
        task_id="end_pipeline"
    )

    start_pipeline >> run_databricks_job >> data_quality_check >> end_pipeline
