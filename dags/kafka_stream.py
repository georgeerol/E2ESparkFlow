import json
import logging
import airflow
import requests
import time
import uuid
from kafka import KafkaProducer
from airflow import DAG
from airflow.operators.python import PythonOperator

# Default arguments for the DAG
default_args = {
    "owner": "George Fouche",
    'start_date': airflow.utils.dates.days_ago(1)
}


def get_data():
    """
    Fetches random user data from an API.

    Returns:
        dict: A dictionary containing user data.
    """
    response = requests.get("https://randomuser.me/api/")
    user_data = response.json()['results'][0]
    return user_data


def format_data(user_data):
    """
    Formats the raw user data into a structured dictionary.

    Args:
        user_data (dict): The raw data of the user.

    Returns:
        dict: A dictionary with formatted user data.
    """
    location = user_data['location']
    address_parts = [
        str(location['street']['number']),
        location['street']['name'],
        location['city'],
        location['state'],
        location['country']
    ]
    formatted_data = {
        'id': str(uuid.uuid4()),
        'first_name': user_data['name']['first'],
        'last_name': user_data['name']['last'],
        'gender': user_data['gender'],
        'address': ', '.join(address_parts),
        'post_code': location['postcode'],
        'email': user_data['email'],
        'username': user_data['login']['username'],
        'dob': user_data['dob']['date'],
        'registered_date': user_data['registered']['date'],
        'phone': user_data['phone'],
        'picture': user_data['picture']['medium']
    }
    return formatted_data


def stream_data():
    """
    Streams formatted user data to a Kafka topic at regular intervals.
    """
    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    start_time = time.time()

    while time.time() < start_time + 60:  # Stream for 1 minute
        try:
            user_data = get_data()
            formatted_data = format_data(user_data)
            producer.send('users_created', json.dumps(formatted_data).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occurred: {e}')


# Defining the DAG
with DAG('user_automation', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )
