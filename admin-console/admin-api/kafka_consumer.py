from confluent_kafka import Consumer, KafkaError
from hdfs import InsecureClient

bootstrap_servers = 'localhost:9092'
group_id = 'my-consumer-group'

hdfs_host = 'http://localhost:9870'  # Replace with your HDFS Namenode address
hdfs_user = 'hadoop'  # Replace with your Hadoop user
hdfs_client = InsecureClient(hdfs_host, user=hdfs_user)

def consume_from_topic(topic_name):
    consumer = Consumer({
        'bootstrap.servers': bootstrap_servers,
        'group.id': group_id,
        'auto.offset.reset': 'earliest'  # Start consuming from the earliest available offset
    })

    consumer.subscribe([topic_name])

    try:
        while True:
            message = consumer.poll(1.0)

            if message is None:
                continue
            if message.error():
                if message.error().code() == KafkaError._PARTITION_EOF:
                    print('Reached end of partition.')
                else:
                    print(f'Error while consuming message: {message.error()}')
            else:
                # Save the received message to HDFS
                message_value = message.value().decode('utf-8')
                hdfs_client.write(f'/path/to/hdfs/folder/{topic_name}', data=message_value, overwrite=False)
                print(f'Received message: {message_value}')
    except KeyboardInterrupt:
        consumer.close()

if __name__ == '__main__':
    topic_name = 'test'
    consume_from_topic(topic_name)
