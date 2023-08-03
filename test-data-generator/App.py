import os
import time
import traceback

import pymongo
from flask import Flask, request, jsonify
from kafka_gen.create_topics import create_init_topics
from kafka_gen.message_publisher import init_user_load, init_movie_load, init_category_load, publish_to_kafka
from log_gen.log_generator import generate_logs
from app_util.Util import UserIdGenerator, MovieIdGenerator
from mongo.review_generator import init_data_load, save_data_to_hdfs, get_data_from_mongodb

app = Flask(__name__)


@app.route('/data-load/kafka/create_init_topics', methods=['POST'])
def data_load_kafka_create_topic():
    try:
        create_init_topics(bootstrap_servers)
        return jsonify({'message': 'kafka topics added successfully'}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': 'Failed to add kafka topics'}), 500


@app.route('/init-data-load/kafka', methods=['POST'])
def init_data_load_kafka():
    try:
        init_category_load(bootstrap_servers)
        init_movie_load(100, movie_id_gen, bootstrap_servers)
        init_user_load(1000, user_id_gen, bootstrap_servers)
        return jsonify({'message': 'Init Kafka Data load initialized'}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': 'Failed to initialize Kafka data load'}), 500


@app.route('/data-load/kafka/publish_message', methods=['POST'])
def data_load_kafka_publish_message():
    try:
        topic = request.args.get("topic")
        data = request.get_json()
        publish_to_kafka(bootstrap_servers, topic, data)
        return jsonify({'message': 'Data published successfully'}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': 'Failed to publish data'}), 500


@app.route('/init-data-load/log', methods=['POST'])
def init_data_load_log():
    try:
        file_name = "/logs/log" + str(time.time_ns()) + ".log"
        generate_logs(file_name, 10000, 0.9)
        return jsonify({'message': 'Log Data load initialized'}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': 'Failed to initialize data load'}), 500


@app.route('/data-load/log', methods=['POST'])
def data_load_log():
    try:
        # Get data from request body
        row_count = int(request.args.get("row_count"))
        info_probability = float(request.args.get("info_probability"))
        file_name = "/logs/log" + str(time.time_ns()) + ".log"
        generate_logs(file_name, row_count, info_probability)

        return jsonify({'message': 'Log Data added successfully'}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': 'Failed to add log data'}), 500


@app.route('/init-data-load/mongo', methods=['POST'])
def init_data_load_mongo():
    try:
        init_data_load(collection, 1000)
        data = get_data_from_mongodb(collection)
        save_data_to_hdfs(hdfs_url, hdfs_user, hdfs_path, data)
        return jsonify({'message': 'Review Data load initialized'}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': 'Failed to initialize Review data load'}), 500

@app.route('/data-load/mongo', methods=['POST'])
def data_load_mongo():
    try:
        # Get data from request body
        row_count = int(request.args.get("review_count"))
        init_data_load(collection, row_count)
        data = get_data_from_mongodb(collection)
        save_data_to_hdfs(hdfs_url, hdfs_user, hdfs_path, data)
        return jsonify({'message': 'Review Data added successfully'}), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': 'Failed to add Review data'}), 500


if __name__ == '__main__':
    user_id_gen = UserIdGenerator()
    movie_id_gen = MovieIdGenerator()
    bootstrap_servers = os.environ.get('KAFKA_SERVER', "kafka:29092")
    client = pymongo.MongoClient(os.environ.get('MONGO_CONNECTION_STRING', "mongodb://mongo:27017/"))
    db = client[os.environ.get('MONGO_DB_NAME', "movies")]
    collection = db[os.environ.get('MONGO_COLLECTION_NAME', "movie_reviews")]
    hdfs_url = os.environ.get('HDFS_URL', "http://namenode:9870")
    hdfs_user = os.environ.get('HDFS_USER', "test_user")
    hdfs_path = os.environ.get('HDFS_PATH', "/data/reviews")
    app.run(host="0.0.0.0", port=8787)
