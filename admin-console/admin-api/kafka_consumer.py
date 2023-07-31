from confluent_kafka import Consumer, KafkaError

# Replace with your Kafka broker(s) host and port
bootstrap_servers = 'localhost:29092'
group_id = 'my-consumer-group'  # Replace with a unique consumer group ID

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
                print(f'Received message: {message.value().decode("utf-8")}')
    except KeyboardInterrupt:
        consumer.close()

if __name__ == '__main__':
    topic_name = 'your-topic-name'  # Replace with the Kafka topic you want to consume from
    consume_from_topic(topic_name)
