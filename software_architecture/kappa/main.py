import os
from diagrams import Diagram, Cluster
from diagrams.onprem.queue import Kafka
from diagrams.onprem.analytics import Spark
from diagrams.generic.database import SQL

def create_kappa_architecture_diagram():

    # Define the directory and file path
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, "kappa_diagram")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")
    
    with Diagram("Kappa Architecture", direction="LR", show=False, outformat="png", filename=output_file_path):
        data_stream = Kafka("Data Stream")
        
        with Cluster("Processing"):
            stream_proc = Spark("Stream Processing")
        
        serving_db = SQL("Serving Database")

        data_stream >> stream_proc >> serving_db

if __name__ == "__main__":
    create_kappa_architecture_diagram()
