from kafka import KafkaConsumer

# Kafka settings
kafka_topic = "users_created"
kafka_server = "broker:29092"

# Initialize Kafka consumer
consumer = KafkaConsumer(
    kafka_topic,
    bootstrap_servers=[kafka_server],
    auto_offset_reset='earliest',  # Start from the earliest message
    group_id='my-group',           # Consumer group ID
    value_deserializer=lambda x: x.decode('utf-8')  # Deserialize messages to UTF-8 strings
)

# Consume messages
for message in consumer:
    print(f"Received message: {message.value}")
