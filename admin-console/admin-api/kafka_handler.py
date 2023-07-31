from confluent_kafka import Producer, KafkaError
from confluent_kafka.admin import AdminClient, NewTopic
from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace with your Kafka broker(s) host and port
bootstrap_servers = 'localhost:9092'

def create_topic(topic_name, num_partitions=1, replication_factor=1):
    admin_client = AdminClient({'bootstrap.servers': bootstrap_servers})
    new_topic = NewTopic(topic_name, num_partitions=num_partitions, replication_factor=replication_factor)
    futures = admin_client.create_topics([new_topic])

    for _, future in futures.items():
        try:
            future.result()
            return f'Topic "{topic_name}" created successfully!'
        except Exception as e:
            return f'Error creating topic: {e}'

def publish_message(topic_name, message):
    producer = Producer({'bootstrap.servers': bootstrap_servers})
    try:
        producer.produce(topic_name, message.encode('utf-8'))
        producer.flush()
        return f'Message published to topic "{topic_name}" successfully!'
    except Exception as e:
        return f'Error publishing message to topic: {e}'

@app.route('/api/kafka/topics', methods=['POST'])
def create_kafka_topic():
    topic_name = request.args.get('topicName')
    num_partitions = int(request.args.get('numPartitions', 1))
    replication_factor = int(request.args.get('replicationFactor', 1))

    result = create_topic(topic_name, num_partitions, replication_factor)
    return jsonify({'message': result})

@app.route('/api/kafka/publish', methods=['POST'])
def publish_kafka_message():
    topic_name = request.args.get('topicName')
    message = request.args.get('message')

    result = publish_message(topic_name, message)
    return jsonify({'message': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
