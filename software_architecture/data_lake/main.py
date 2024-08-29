import os
from diagrams import Diagram, Cluster
from diagrams.aws.storage import S3
from diagrams.onprem.analytics import Spark
from diagrams.onprem.analytics import Databricks

def create_data_lake_diagram():
    # Define the directory and file path
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, "data_lake_diagram")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")

    with Diagram("Data Lake", direction="LR", show=False, outformat="png", filename=output_file_path):
        raw_data = S3("Raw Data")
        
        with Cluster("Processing"):
            etl = Spark("ETL Jobs")
            catalog = Databricks("Data Catalog")
            databricks = Databricks("Analytics & ML")

        raw_data >> etl >> catalog >> databricks

if __name__ == "__main__":
    create_data_lake_diagram()
