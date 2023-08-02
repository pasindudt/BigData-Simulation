from datetime import datetime, timedelta

from kafka import KafkaProducer
import json
import random

used_usernames = set()

first_names_file_path = "/app/kafka_gen/first_names"
last_names_file_path = "/app/kafka_gen/last_names"
movies_file_path = "/app/kafka_gen/movies"
categories_file_path = "/app/kafka_gen/categories"

first_names_array = []
last_names_array = []
movies_array = []
categories_array = []

with open(first_names_file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        first_names_array.append(line)

with open(last_names_file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        last_names_array.append(line)

with open(movies_file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        movie = line.split('|')[0].strip()
        genre = line.split('|')[1].strip()
        movies_array.append((movie, genre))

with open(categories_file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        cat_id = line.split('|')[0].strip()
        cat_name = line.split('|')[1].strip()
        categories_array.append((cat_id, cat_name))


def generate_user_id(user_generator):
    return user_generator.get_next_user_id()


def generate_movie_id(movie_generator):
    return movie_generator.get_next_movie_id()


def generate_username():
    username = random.choice(first_names_array) + ' ' + random.choice(last_names_array)
    while username in used_usernames:
        username = random.choice(first_names_array) + ' ' + random.choice(last_names_array)
    used_usernames.add(username)
    return username


def generate_random_date(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    days_range = (end_date - start_date).days
    random_days = random.randint(0, days_range)
    random_date = start_date + timedelta(days=random_days)
    random_date_str = random_date.strftime("%Y-%m-%d")

    return random_date_str


def generate_user_message(action, user_id_gen):
    message = {
        "action": action,
        "entity": "user",
        "data": {}
    }
    message["data"]["user_id"] = generate_user_id(user_id_gen)
    message["data"]["username"] = generate_username()
    message["data"]["email"] = f'{message["data"]["username"]}@example.com'

    return json.dumps(message)


def generate_movie_message(action, movie_id_gen):
    message = {
        "action": action,
        "entity": "movie",
        "data": {}
    }
    message["data"]["movie_id"] = generate_movie_id(movie_id_gen)
    movie_name, category = movies_array[movie_id_gen.counter-1]
    message["data"]["title"] = movie_name
    message["data"]["release_date"] = generate_random_date("1930-01-01", "2023-01-01")
    message["data"]["category"] = category

    return json.dumps(message)


def generate_category_message(action, _cat_id, _name):
    message = {
        "action": action,
        "entity": "category",
        "data": {}
    }
    message["data"]["category_id"] = _cat_id
    message["data"]["name"] = _name

    return json.dumps(message)


def publish_to_kafka(bootstrap_servers_url, topic_name, message):
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers_url,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send(topic_name, value=json.loads(message))

    producer.flush()
    producer.close()


def init_user_load(count, user_id_gen, bootstrap_servers):
    for _ in range(count):
        message = generate_user_message("create", user_id_gen)
        publish_to_kafka(bootstrap_servers, "user", message)


def init_movie_load(count, movie_id_gen, bootstrap_servers):
    for _ in range(count):
        message = generate_movie_message("create", movie_id_gen)
        publish_to_kafka(bootstrap_servers, "movie", message)


def init_category_load(bootstrap_servers):
    for _cat_id, _cat_name in categories_array:
        message = generate_category_message("create", _cat_id, _cat_name)
        publish_to_kafka(bootstrap_servers, "category", message)