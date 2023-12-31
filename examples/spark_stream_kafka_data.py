from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Create a Spark Session
spark = SparkSession.builder \
    .appName("KafkaReadWithSchema") \
    .getOrCreate()

# Kafka Configuration
kafka_topic_name = "users_created"
kafka_bootstrap_servers = "broker:29092"

# Define the schema
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

# Read from Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic_name) \
    .option("startingOffsets", "earliest") \
    .load()

# Assuming the value in Kafka is a JSON string matching the schema
df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# Output (prints on console)
query = df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
