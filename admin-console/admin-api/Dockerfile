# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python dependencies
RUN pip install --no-cache-dir confluent-kafka flask

# Expose the port on which your Flask server runs (replace with the port number used in your Flask app)
EXPOSE 5000

# Start the Kafka consumer service in the background
CMD ["python", "kafka_consumer.py", "&"]

# Run the Flask app when the container starts
CMD ["python", "kafka_handler.py"]
