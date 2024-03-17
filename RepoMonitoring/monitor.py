from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.email import send_email
from repo import GitHub
import os, json

default_args = {
    'owner': 'bobby',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 12),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

URL = "https://github.com/huggingface/transformers"

def monitor_stars(**kwargs):
    gh = GitHub(URL)
    metadata = gh.get_repo_metadata()
    current_stars = metadata.get("stargazers_count")

    directory = os.path.dirname(os.path.abspath(__file__))
    filename = URL.replace('https:','').replace('/', '_')
    fully_qualified_filename = f"{directory}\data\{filename}"

    if os.path.exists(fully_qualified_filename):
        with open(fully_qualified_filename, 'r') as file:
            previous_metadata = json.load(file)
    else:
        previous_metadata = None
    
    previous_stars = previous_metadata.get("stargazers_count")
    latest_stars = current_stars - previous_stars

    if latest_stars > 10000:
        subject = f"GitHub Alert for {URL}"
        content = f"The {URL} repository has received {latest_stars} stars since last check"
        to='masked@masked.com'

        send_email(to=to, subject=subject, html_content=content)

    gh.save_metadata(metadata, fully_qualified_filename)

with DAG('github_repo_monitor', 
         default_args=default_args, 
         schedule_interval='@daily', 
         catchup=False
        ) as dag:

    monitor_and_alert = PythonOperator(
        task_id='monitor_stars',
        python_callable=monitor_stars,
        provide_context=True,
    )

    monitor_and_alert
