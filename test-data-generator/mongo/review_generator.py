import random

# Lists of adjectives and review structures
import re
from datetime import datetime

import pymongo
from hdfs import InsecureClient

positive_adjectives = ["amazing", "brilliant", "excellent", "fantastic", "impressive", "outstanding",
                       "remarkable", "superb", "terrific", "wonderful"]
negative_adjectives = ["boring", "disappointing", "dull", "awful", "terrible", "horrible", "uninspiring",
                       "mediocre", "predictable", "disliked"]
neutral_adjectives = ["average", "decent", "okay", "standard", "moderate", "satisfactory", "passable",
                      "indifferent", "mixed", "middling"]

# Generate 25 review structures for each sentiment
positive_reviews = [
                       f"I thought it was {adj}!" for adj in positive_adjectives
                   ] + [
                       f"It's a {adj} movie." for adj in positive_adjectives
                   ] + [
                       f"If you haven't seen it, you're missing out. It's {adj}!" for adj in
                       positive_adjectives
                   ] + [
                       f"Wow! Just wow! It is {adj}." for adj in positive_adjectives
                   ] + [
                       f"I can't get enough of it. It's so {adj}!" for adj in positive_adjectives
                   ] + [
                       f"I absolutely loved it. {adj}!" for adj in positive_adjectives
                   ] + [
                       f"The {adj} storytelling kept me engaged throughout." for adj in positive_adjectives
                   ] + [
                       f"The acting was {adj}!" for adj in positive_adjectives
                   ] + [
                       f"The movie is a {adj} example of its genre." for adj in positive_adjectives
                   ] + [
                       f"I was blown away by how {adj} it was." for adj in positive_adjectives
                   ] + [
                       f"{adj.capitalize()} performances elevated the movie to greatness." for adj in
                       positive_adjectives
                   ] + [
                       f"The film is a {adj} masterpiece." for adj in positive_adjectives
                   ] + [
                       f"An all-around {adj} movie that I'll watch again." for adj in positive_adjectives
                   ] + [
                       f"It's a must-see, {adj} film." for adj in positive_adjectives
                   ] + [
                       f"The movie's {adj} visuals were a feast for the eyes." for adj in positive_adjectives
                   ] + [
                       f"I couldn't have asked for a more {adj} ending." for adj in positive_adjectives
                   ] + [
                       f"The movie's {adj} soundtrack added to the overall experience." for adj in
                       positive_adjectives
                   ] + [
                       f"It left me with a {adj} feeling of satisfaction." for adj in positive_adjectives
                   ] + [
                       f"The movie's {adj} cinematography was captivating." for adj in positive_adjectives
                   ] + [
                       f"{adj.capitalize()} direction and great performances make it worth watching." for adj
                       in positive_adjectives
                   ] + [
                       f"The film is {adj} in every aspect." for adj in positive_adjectives
                   ] + [
                       f"I was impressed by how {adj} the movie turned out to be." for adj in
                       positive_adjectives
                   ] + [
                       f"I have nothing but {adj} things to say about it." for adj in positive_adjectives
                   ] + [
                       f"The movie is an absolute {adj}!" for adj in positive_adjectives
                   ] + [
                       f"{adj.capitalize()} entertainment from start to finish." for adj in
                       positive_adjectives
                   ]

negative_reviews = [
                       f"I thought it was {adj}." for adj in negative_adjectives
                   ] + [
                       f"It's a {adj} movie." for adj in negative_adjectives
                   ] + [
                       f"I didn't enjoy it. It's {adj}." for adj in negative_adjectives
                   ] + [
                       f"I found it to be {adj}." for adj in negative_adjectives
                   ] + [
                       f"Unfortunately, it is {adj}." for adj in negative_adjectives
                   ] + [
                       f"The movie was a {adj} mess." for adj in negative_adjectives
                   ] + [
                       f"{adj.capitalize()} acting and a weak plot ruined the experience for me." for adj in
                       negative_adjectives
                   ] + [
                       f"The {adj} direction made it hard to watch." for adj in negative_adjectives
                   ] + [
                       f"I regret watching it. {adj} movie." for adj in negative_adjectives
                   ] + [
                       f"The movie was completely {adj} and lacked originality." for adj in
                       negative_adjectives
                   ] + [
                       f"The film's {adj} execution was disappointing." for adj in negative_adjectives
                   ] + [
                       f"A {adj} movie that fails to live up to its potential." for adj in negative_adjectives
                   ] + [
                       f"It was a {adj} attempt at storytelling." for adj in negative_adjectives
                   ] + [
                       f"The movie's {adj} dialogue made it hard to stay engaged." for adj in
                       negative_adjectives
                   ] + [
                       f"The movie left me feeling {adj} and unimpressed." for adj in negative_adjectives
                   ] + [
                       f"I couldn't wait for it to end. {adj} experience." for adj in negative_adjectives
                   ] + [
                       f"It lacked any redeeming {adj} qualities." for adj in negative_adjectives
                   ] + [
                       f"The movie's {adj} editing disrupted the flow." for adj in negative_adjectives
                   ] + [
                       f"I was disappointed by how {adj} the movie turned out to be." for adj in
                       negative_adjectives
                   ] + [
                       f"The film is {adj} in every aspect." for adj in negative_adjectives
                   ] + [
                       f"I have nothing but {adj} things to say about it." for adj in negative_adjectives
                   ] + [
                       f"The movie is an absolute {adj}!" for adj in negative_adjectives
                   ] + [
                       f"{adj.capitalize()} entertainment from start to finish." for adj in
                       negative_adjectives
                   ]

neutral_reviews = [
                      f"I thought it was {adj}." for adj in neutral_adjectives
                  ] + [
                      f"It's a {adj} movie." for adj in neutral_adjectives
                  ] + [
                      f"I have mixed feelings about it. It's {adj}." for adj in neutral_adjectives
                  ] + [
                      f"It is an {adj} movie." for adj in neutral_adjectives
                  ] + [
                      f"It is quite {adj}." for adj in neutral_adjectives
                  ] + [
                      f"The movie was {adj} overall." for adj in neutral_adjectives
                  ] + [
                      f"It left me feeling {adj}." for adj in neutral_adjectives
                  ] + [
                      f"{adj.capitalize()}, I neither loved nor hated it." for adj in neutral_adjectives
                  ] + [
                      f"The film has its moments, but it's mostly {adj}." for adj in neutral_adjectives
                  ] + [
                      f"The movie's {adj} storyline failed to impress." for adj in neutral_adjectives
                  ] + [
                      f"I'm indifferent to it. {adj} movie." for adj in neutral_adjectives
                  ] + [
                      f"The movie's pacing felt {adj} and inconsistent." for adj in neutral_adjectives
                  ] + [
                      f"A {adj} attempt at a compelling narrative." for adj in neutral_adjectives
                  ] + [
                      f"The film is a {adj} mix of good and bad." for adj in neutral_adjectives
                  ] + [
                      f"The movie is enjoyable, but ultimately {adj}." for adj in neutral_adjectives
                  ] + [
                      f"I had high hopes, but it fell {adj} of my expectations." for adj in neutral_adjectives
                  ] + [
                      f"The movie left me feeling {adj} and unsure." for adj in neutral_adjectives
                  ] + [
                      f"The film's ending was {adj} and open to interpretation." for adj in neutral_adjectives
                  ] + [
                      f"I can't quite put my finger on it, but something felt {adj} about the movie." for adj
                      in neutral_adjectives
                  ] + [
                      f"{adj.capitalize()} performances and a decent plot made it watchable." for adj in
                      neutral_adjectives
                  ] + [
                      f"It was an {adj} experience that didn't leave a lasting impact." for adj in
                      neutral_adjectives
                  ] + [
                      f"The movie's {adj} special effects were notable." for adj in neutral_adjectives
                  ] + [
                      f"It had its moments, but it was mostly {adj}." for adj in neutral_adjectives
                  ] + [
                      f"The movie's message was {adj} and thought-provoking." for adj in neutral_adjectives
                  ] + [
                      f"The film is a {adj} choice for a casual movie night." for adj in neutral_adjectives
                  ]

review_structures = positive_reviews + negative_reviews + neutral_reviews


def generate_random_review():
    review_structure = random.choice(review_structures)
    return review_structure


def get_user():
    return f"user_{random.randint(0, 100):04d}"


def get_movie():
    return f"movie_{random.randint(0, 100):04d}"


# client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
# db = client[MONGO_DB_NAME]
# collection = db[MONGO_COLLECTION_NAME]

def init_data_load(collection, count):
    for _ in range(count):
        add_review(collection)


def add_review(collection):
    review = generate_random_review()
    user = get_user()
    movie = get_movie()
    timestamp = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    review = {
        "user_id": user,
        "movie_id": movie,
        "review": review,
        "time_Stamp": timestamp
    }

    collection.insert_one(review)


def get_data_from_mongodb(collection, query=None):
    try:
        # Execute the query and retrieve data
        if query is None:
            data = collection.find()
        else:
            data = collection.find(query)

        return list(data)
    except Exception as e:
        print("Error:", e)


def extract_values(input_string):
    # Define the regular expression pattern to match the required fields
    pattern = r"'user_id': '(\w+)', 'movie_id': '([^']*)', 'review': '([^']*)', 'time_Stamp': '([^']*)'"

    # Find all occurrences of the pattern in the input string
    matches = re.findall(pattern, input_string)

    # Extract and format the values for each match
    formatted_strings = []
    for match in matches:
        user_id, movie_id, review, time_stamp = match
        formatted_strings.append(f"{user_id},{movie_id},{review}")

    # Join the formatted strings with newlines and return the result
    return '\n'.join(formatted_strings)


def save_data_to_hdfs(hdfs_url, hdfs_user, hdfs_file_path, data):
    # Create an HDFS client
    client = InsecureClient(hdfs_url, user=hdfs_user, timeout=300)

    try:
        # Convert the data to a newline-separated string
        data_string = "\n".join(map(str, data))
        print(data_string)

        output_string = extract_values(data_string)
        print(output_string)

        # Upload the data to HDFS
        with client.write(hdfs_file_path, overwrite=True) as hdfs_file:
            hdfs_file.write(output_string.encode())
        print("Data saved to HDFS successfully.")
    except Exception as e:
        print("Error:", e)