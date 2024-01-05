from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Create a Spark Session with Cassandra configuration
spark = SparkSession.builder \
    .appName("KafkaToCassandra") \
    .config("spark.cassandra.connection.host", "cassandra") \
    .config("spark.cassandra.connection.port", "9042") \
    .config("spark.cassandra.auth.username", "cassandra") \
    .config("spark.cassandra.auth.password", "cassandra") \
    .getOrCreate()

# Initialize Cassandra connection
auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
cluster = Cluster(['cassandra'], port=9042, auth_provider=auth_provider)
session = cluster.connect()

# Create keyspace and table in Cassandra
keyspace_query = """
CREATE KEYSPACE IF NOT EXISTS user_data WITH replication = {
  'class': 'SimpleStrategy', 'replication_factor': '1'
};
"""

table_query = """
CREATE TABLE IF NOT EXISTS user_data.users (
    id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    gender TEXT,
    address TEXT,
    postcode INT,
    email TEXT,
    username TEXT,
    dob TEXT,
    registered TEXT,
    phone TEXT,
    picture TEXT
);
"""

session.execute(keyspace_query)
session.execute(table_query)
session.shutdown()

# Kafka Configuration
kafka_topic_name = "users_created"
kafka_bootstrap_servers = "broker:29092"

# Define the schema for the data to be processed
schema = StructType([
    StructField("id", StringType(), False),
    StructField("first_name", StringType(), False),
    StructField("last_name", StringType(), False),
    StructField("gender", StringType(), False),
    StructField("address", StringType(), False),
    StructField("postcode", IntegerType(), False),
    StructField("email", StringType(), False),
    StructField("username", StringType(), False),
    StructField("dob", StringType(), False),
    StructField("registered", StringType(), False),
    StructField("phone", StringType(), False),
    StructField("picture", StringType(), False)
])

# Read data from Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic_name) \
    .option("startingOffsets", "earliest") \
    .load()

# Parse the incoming data assuming it's in JSON format
df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# Define Cassandra Table Details
cassandra_keyspace = "user_data"
cassandra_table = "users"

# Write the processed data to Cassandra
query = df.writeStream \
    .format("org.apache.spark.sql.cassandra") \
    .option("keyspace", cassandra_keyspace) \
    .option("table", cassandra_table) \
    .option("checkpointLocation", "/tmp/checkpoint") \
    .start()

query.awaitTermination()
