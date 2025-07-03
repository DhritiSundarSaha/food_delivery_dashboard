from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
from faker import Faker
import random
import pandas as pd
from sqlalchemy import create_engine

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def generate_and_load():
    fake = Faker()
    engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres:5432/food_delivery')
    # simple insertion: generate 100 deliveries each run
    deliveries = []
    now = datetime.now()
    for i in range(100):
        user = random.randint(1, 300)
        rest = random.randint(1, 50)
        pickup = now - timedelta(minutes=random.randint(30, 60))
        duration = random.randint(10, 60)
        delivered = pickup + timedelta(minutes=duration)
        cancelled = random.random() < 0.07
        deliveries.append({'user_id': user,
                           'restaurant_id': rest,
                           'pickup_time': pickup,
                           'delivered_time': None if cancelled else delivered,
                           'is_cancelled': cancelled,
                           'delivery_fee': round(random.uniform(2, 8), 2)})
    df = pd.DataFrame(deliveries)
    df.to_sql('deliveries', engine, if_exists='append', index=False)

with DAG('food_delivery_etl', start_date=datetime(2025,7,1), schedule_interval='@hourly', default_args=default_args, catchup=False) as dag:
    t1 = BashOperator(
        task_id='check_postgres',
        bash_command='echo "Postgres is ready"'
    )
    t2 = PythonOperator(
        task_id='generate_load_data',
        python_callable=generate_and_load
    )
    t1 >> t2
