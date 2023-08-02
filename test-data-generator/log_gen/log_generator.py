import logging
import random
from datetime import datetime

import docker
import os


# List of users and movie categories for simulation
def get_user():
    return f"user_{random.randint(0, 100):04d}"


def get_movie():
    return f"movie_{random.randint(0, 100):04d}"


def get_category():
    return f"category_{random.randint(0, 16):04d}"


def write_to_custom_log(level, message, file):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {level} - {message}\n"
    file.write(log_entry)


# Simulate log generation
def generate_logs(file_name, row_count, info_probability=0.8):
    with open(file_name, "a") as file:
        for _ in range(row_count):
            if random.random() <= info_probability:
                # Generate INFO log
                user = get_user()
                movie = get_movie()
                category = get_category()
                action = random.choice(
                    ["logged in successfully.", "searched for", "visited the", "started watching",
                     "paused watching", "resumed watching", "rated the"])
                if "watching" in action:
                    log_message = f'User "{user}" {action} "{movie}"'
                elif "logged" in action:
                    log_message = f'User "{user}" {action}'
                elif "searched" in action:
                    log_message = f'User "{user}" {action} "{category}"'
                elif "rated" in action:
                    log_message = f'User "{user}" {action} "{movie}"'
                write_to_custom_log("INFO", log_message, file)
            else:
                # Generate ERROR log
                error_codes = [404, 500, 502, 503]
                error_code = random.choice(error_codes)
                log_message = f'An unexpected error occurred while processing the user request. Error code: {error_code}.'
                write_to_custom_log("ERROR", log_message, file)


def get_container_by_name(client, container_name):
    for container in client.containers.list():
        if container.name == container_name:
            return container
    return None


def copy_file_to_container(container_name, source_path, destination_path):
    client = docker.from_env()

    # Get the container by name
    container = get_container_by_name(client, container_name)
    if not container:
        print(f"Error: Container with name '{container_name}' not found.")
        return

    # Verify if the source file exists
    if not os.path.isfile(source_path):
        print(f"Error: Source file '{source_path}' not found.")
        return

    # Read the content of the file
    with open(source_path, 'rb') as f:
        content = f.read()

    # Copy the file content to the container
    try:
        exec_command = f"echo -n '{content.decode('utf-8')}' > {destination_path}"
        exec_response = container.exec_run(cmd=["/bin/sh", "-c", exec_command])
        print(f"File '{source_path}' copied to container '{container_name}' at '{destination_path}'.")
        print(exec_response)
    except docker.errors.APIError as e:
        print(f"Error copying the file to the container: {e}")
    finally:
        client.close()