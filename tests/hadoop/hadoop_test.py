from hdfs import InsecureClient

def connect_to_hdfs(url, user):
    try:
        client = InsecureClient(url)
        print("Connected to HDFS successfully.")
        return client
    except Exception as e:
        print(f"Error connecting to HDFS: {e}")
        return None

def list_files_in_hdfs(client, path):
    try:
        file_list = client.list(path)
        print(f"Files and directories in {path}:")
        for file in file_list:
            print(file)
    except Exception as e:
        print(f"Error listing files in HDFS: {e}")

if __name__ == "__main__":

    hdfs_url = 'http://localhost:9870'
    hdfs_username = 'your_hdfs_username'
    hdfs_path = '/'

    hdfs_client = connect_to_hdfs(hdfs_url, hdfs_username)

    if hdfs_client:
        list_files_in_hdfs(hdfs_client, hdfs_path)
