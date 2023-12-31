import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

# Initialize the DAG with default arguments and schedule
dag = DAG(
    dag_id="sparking_flow",
    default_args={
        "owner": "George Fouche",
        "start_date": airflow.utils.dates.days_ago(1)
    },
    schedule_interval="@daily"
)

# Define a PythonOperator for starting the job
start = PythonOperator(
    task_id="start",
    python_callable=lambda: print("Jobs started"),
    dag=dag
)

# Define a SparkSubmitOperator for running a Python Spark job
python_job = SparkSubmitOperator(
    task_id="python_job",
    conn_id="spark-conn",
    application="jobs/python/wordcountjob.py",
    dag=dag
)

# Define a SparkSubmitOperator for running a Java Spark job
java_job = SparkSubmitOperator(
    task_id="java_job",
    conn_id="spark-conn",
    application="jobs/java/spark-job/target/spark-job-1.0-SNAPSHOT.jar",
    java_class="com.airscholar.spark.WordCountJob",
    dag=dag
)

# Define a PythonOperator for signaling the end of the job
end = PythonOperator(
    task_id="end",
    python_callable=lambda: print("Jobs completed successfully"),
    dag=dag
)

# Define the task dependencies
start >> [python_job, java_job] >> end
