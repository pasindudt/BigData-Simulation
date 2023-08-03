from pymongo import MongoClient

uri = 'localhost:27017'

def test_connection():
    try:
        # Connect to the MongoDB cluster
        client = MongoClient(uri)

        # Check if the connection was successful
        db_names = client.list_database_names()
        print('Connection successful!')

        # Print the list of available databases
        print('Available databases:', db_names)

        # Close the connection
        client.close()
        print('Connection closed.')
    except Exception as e:
        # Print an error message if the connection fails
        print('Connection failed:', e)

# Call the function to test the connection
test_connection()
