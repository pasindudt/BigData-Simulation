import pymongo
from hdfs import InsecureClient
import re

def get_data_from_mongodb(database_name, collection_name, query=None):
    # Replace 'mongodb://localhost:27017/' with your MongoDB connection string
    client = pymongo.MongoClient('mongodb://mongo:27017/')

    try:
        # Access the specified database and collection
        db = client[database_name]
        collection = db[collection_name]

        # Execute the query and retrieve data
        if query is None:
            data = collection.find()
        else:
            data = collection.find(query)

        return list(data)
    except Exception as e:
        print("Error:", e)
    finally:
        client.close()

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

def extract_values(input_string):
    # Define the regular expression pattern to match the required fields
    pattern = r"'user_id': '(\w+)', 'movie_name': '([^']*)', 'review_comment': '([^']*)', 'time_Stamp': '([^']*)'"

    # Find all occurrences of the pattern in the input string
    matches = re.findall(pattern, input_string)

    # Extract and format the values for each match
    formatted_strings = []
    for match in matches:
        user_id, movie_name, review_comment, time_stamp = match
        formatted_strings.append(f"{user_id}, {movie_name}, {review_comment}, {time_stamp}")

    # Join the formatted strings with newlines and return the result
    return '\n'.join(formatted_strings)

if __name__ == "__main__":
    # Replace 'mongodb://localhost:27017/' with your MongoDB connection string
    mongodb_url = 'mongo:27017'
    # Replace 'your_database_name' and 'your_collection_name' with actual names
    database_name = 'movie_reviews'
    collection_name = 'user_reviews'

    # Replace 'http://localhost:50070' with the HDFS namenode URL
    hdfs_url = 'http://namenode:9870'
    # Replace 'your_hdfs_user' with your HDFS username (if authentication is enabled)
    hdfs_user = 'your_hdfs_username'
    # Replace 'hdfs_file_path' with the destination path on HDFS where you want to save the data
    # hdfs_file_path = '/hadoop/dfs/data/data1.txt'
    hdfs_file_path = '/data2.txt'

    # Retrieve data from MongoDB
    data = get_data_from_mongodb(database_name, collection_name)

    # Save data to HDFS
    save_data_to_hdfs(hdfs_url, hdfs_user, hdfs_file_path, data)
