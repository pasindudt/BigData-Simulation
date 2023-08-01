from confluent_kafka import Producer, KafkaError
from confluent_kafka.admin import AdminClient, NewTopic
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Replace with your Kafka broker(s) host and port
bootstrap_servers = 'localhost:9092'

def list_topics():
    admin_client = AdminClient({'bootstrap.servers': bootstrap_servers})
    metadata = admin_client.list_topics(timeout=5)
    topics = [topic for topic in metadata.topics.keys() if not topic.startswith('__')]
    return topics

def create_topic(topic_name, num_partitions=1, replication_factor=1):
    admin_client = AdminClient({'bootstrap.servers': bootstrap_servers})
    new_topic = NewTopic(topic_name, num_partitions=num_partitions, replication_factor=replication_factor)
    futures = admin_client.create_topics([new_topic])

    for topic, future in futures.items():
        try:
            future.result()  # Wait for topic creation to complete
        except Exception as e:
            return f'Error creating topic "{topic}": {e}'

    return f'Topic "{topic_name}" created successfully!'

def publish_message(topic_name, message):
    producer = Producer({'bootstrap.servers': bootstrap_servers})
    try:
        producer.produce(topic_name, message.encode('utf-8'))
        producer.flush()
        return f'Message published to topic "{topic_name}" successfully!'
    except Exception as e:
        return f'Error publishing message to topic "{topic_name}": {e}'

@app.route('/api/kafka/topics', methods=['GET'])
def get_kafka_topics():
    topics = list_topics()
    return jsonify({'topics': topics})

@app.route('/api/kafka/topics', methods=['POST'])
def create_kafka_topic():
    data = request.json  # Get the data from the request body

    topic_name = data.get('topicName')
    num_partitions = int(data.get('numPartitions', 1))
    replication_factor = int(data.get('replicationFactor', 1))

    result = create_topic(topic_name, num_partitions, replication_factor)
    return jsonify({'message': result})

@app.route('/api/kafka/publish', methods=['POST'])
def publish_kafka_message():
    data = request.json

    topic_name = data.get('topicName')
    message = data.get('message')

    if not topic_name or not message:
        return jsonify({'message': 'Please provide both topicName and message in the request.'}), 400

    result = publish_message(topic_name, message)
    return jsonify({'message': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
