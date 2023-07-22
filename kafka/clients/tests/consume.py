from kafka import KafkaConsumer, KafkaAdminClient

# Kafka broker settings
bootstrap_servers = 'localhost:29092'
topic_name = 'test_topic'

# Create a Kafka AdminClient to manage topics
admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

# Consuming messages from the topic
consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers, group_id='test_group')

print("Consuming messages:")
for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")

# Close the consumer
consumer.close()
