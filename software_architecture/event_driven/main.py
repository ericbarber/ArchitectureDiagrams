import os
from diagrams import Diagram, Cluster
from diagrams.onprem.queue import Kafka
from diagrams.onprem.compute import Server
from diagrams.generic.database import SQL
# Additinoal Imports

def create_architecture_diagram():

    # Define the directory and file path
    design_name = "event driven"
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, f"{design_name.replace(' ', '_')}_diagram")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")
    
    with Diagram(f"{design_name.title()} Architecture", direction="LR", show=False, outformat="png", filename=output_file_path):
        # Architecture diagrams
        producer = Server("Event Producer")
        event_broker = Kafka("Event Broker")
        
        with Cluster("Event Consumers"):
            consumer1 = Server("Consumer 1")
            consumer2 = Server("Consumer 2")
        
        with Cluster("Data Storage"):
            db = SQL("Event Data Store")

        producer >> event_broker >> [consumer1, consumer2]
        consumer1 >> db
        consumer2 >> db

if __name__ == "__main__":
    create_architecture_diagram()
