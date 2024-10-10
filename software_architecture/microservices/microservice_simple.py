import os
from diagrams import Diagram, Cluster
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server
from diagrams.onprem.queue import Kafka
from diagrams.onprem.network import Nginx
# Additinoal Imports

def create_architecture_diagram():

    # Define the directory and file path
    design_name = "microservices"
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, f"{design_name.replace(' ', '_')}_diagram")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")
    
    with Diagram(f"{design_name.title()} Architecture", direction="LR", show=False, outformat="png", filename=output_file_path):
        # Architecture diagrams
        client = Client("Client")
        api_gateway = Nginx("API Gateway")
        
        with Cluster("Microservices"):
            service1 = Server("Service 1")
            service2 = Server("Service 2")
            service3 = Server("Service 3")

        message_broker = Kafka("Message Broker")

        client >> api_gateway >> [service1, service2, service3] >> message_broker


if __name__ == "__main__":
    create_architecture_diagram()
