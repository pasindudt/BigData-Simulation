from kafka import KafkaAdminClient
from kafka.admin import NewTopic

def create_init_topics(bootstrap_servers):
    admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

    topic_list = [NewTopic(name="user", num_partitions=1, replication_factor=1),
                  NewTopic(name="movie", num_partitions=1, replication_factor=1),
                  NewTopic(name="category", num_partitions=1, replication_factor=1)]

    admin_client.create_topics(new_topics=topic_list, validate_only=False)
