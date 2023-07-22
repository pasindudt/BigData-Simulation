from kafka import KafkaProducer, KafkaAdminClient
import time

# Kafka broker settings
bootstrap_servers = 'localhost:29092'
topic_name = 'test_topic'

# Create a Kafka AdminClient to manage topics
admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

# Publishing messages to the topic
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

messages_to_publish = ["Message 1", "Message 2", "Message 3"]

for message in messages_to_publish:
    producer.send(topic_name, message.encode('utf-8'))
    print(f"Published: {message}")
    time.sleep(1)

# Wait for the messages to be sent
producer.flush()
producer.close()