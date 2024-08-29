from diagrams import Diagram, Cluster
from diagrams.onprem.client import User
from diagrams.onprem.compute import Server
from diagrams.onprem.queue import Kafka
from diagrams.onprem.database import Cassandra
from diagrams.onprem.analytics import Spark

import os

def create_pubsub_diagram():
    # Define the directory and file path
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, "pubsub_diagram")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")

    with Diagram("Pub/Sub System", direction="LR", show=False, outformat="png", filename=output_file_path):
        with Cluster("Publishers"):
            publisher1 = User("Publisher 1")
            publisher2 = Server("Publisher 2")
        
        with Cluster("Pub/Sub System"):
            topic = Kafka("Topic")
        
        with Cluster("Subscribers"):
            subscriber1 = Server("Subscriber 1")
            subscriber2 = Server("Subscriber 2")

        with Cluster("Data Processing & Storage"):
            processor = Spark("Real-time Processor")
            db = Cassandra("Database")
        
        # Publishers send messages to the topic
        publisher1 >> topic
        publisher2 >> topic

        # Subscribers receive messages from the topic
        topic >> subscriber1
        topic >> subscriber2

        # Real-time processing and storage
        topic >> processor >> db

if __name__ == "__main__":
    create_pubsub_diagram()

