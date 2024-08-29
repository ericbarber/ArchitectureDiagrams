import os
from diagrams import Diagram, Cluster
from diagrams.onprem.queue import Kafka
from diagrams.onprem.analytics import Spark, Databricks
from diagrams.generic.database import SQL

def create_lambda_architecture_diagram():

    # Define the directory and file path
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, "lambda_diagram")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")
    
    with Diagram("Lambda Architecture", direction="LR", show=False, outformat="png", filename=output_file_path):
        with Cluster("Data Sources"):
            data = Kafka("Data Stream")
        
        with Cluster("Batch Layer"):
            databricks = Databricks("Catalog")
            batch_proc = Spark("Batch Processing")
        
        with Cluster("Speed Layer"):
            stream_proc = Spark("Stream Processing")

        with Cluster("Serving Layer"):
            sql_db = SQL("Serving Database")

        data >> [batch_proc, stream_proc]
        batch_proc >> databricks >> sql_db
        stream_proc >> sql_db

if __name__ == "__main__":
    create_lambda_architecture_diagram()
