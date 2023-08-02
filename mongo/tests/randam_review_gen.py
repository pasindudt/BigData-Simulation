from datetime import datetime
import random
import string
import pymongo

# MongoDB connection details
MONGO_CONNECTION_STRING = "mongodb://mongo:27017/"
MONGO_DB_NAME = "movie_reviews"
MONGO_COLLECTION_NAME = "user_reviews"

# Function to generate a random user ID
def generate_user_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# Function to generate a random movie name
def generate_movie_name():
    movie_names = [
        "The Shawshank Redemption",
        "The Godfather",
        "The Dark Knight",
        "Pulp Fiction",
        "Inception",
        "The Matrix",
        "Forrest Gump",
        "The Lord of the Rings: The Return of the King",
        "Fight Club",
        "Goodfellas",
    ]
    return random.choice(movie_names)

# Function to generate a random review comment
def generate_review_comment():
    good_comments = [
        "Excellent movie!",
        "Loved it!",
        "Great storyline.",
        "Amazing performances.",
        "Highly recommended.",
    ]

    bad_comments = [
        "Disappointing.",
        "Waste of time.",
        "Weak plot.",
        "Bad acting.",
        "Not worth watching.",
    ]

    return random.choice(good_comments + bad_comments)

# Function to generate and save user reviews
def generate_user_reviews(num_reviews):
    client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
    db = client[MONGO_DB_NAME]
    collection = db[MONGO_COLLECTION_NAME]

    for _ in range(num_reviews):
        user_id = generate_user_id()
        movie_name = generate_movie_name()
        review_comment = generate_review_comment()
        timestamp = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

        review = {
            "user_id": user_id,
            "movie_name": movie_name,
            "review_comment": review_comment,
            "time_Stamp": timestamp
        }

        print(review)

        collection.insert_one(review)

    client.close()
    print(f"{num_reviews} user reviews generated and saved to MongoDB.")

if __name__ == "__main__":
    num_reviews_to_generate = 10  # Change this to the desired number of reviews
    generate_user_reviews(num_reviews_to_generate)
