from kafka import KafkaAdminClient
from kafka.admin import NewTopic

# Kafka broker settings
bootstrap_servers = 'localhost:29092'
topic_name = 'test_topic'

# Create a Kafka AdminClient to manage topics
admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

# Create a topic with one partition and a replication factor of 1 (for testing)
topic_list = [NewTopic(name=topic_name, num_partitions=1, replication_factor=1)]
admin_client.create_topics(new_topics=topic_list, validate_only=False)
