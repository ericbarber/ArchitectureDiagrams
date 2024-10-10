import os
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.monitoring import Grafana
from diagrams.onprem.analytics import Superset, Hive, Presto, Spark, Hadoop, Databricks
from diagrams.onprem.container import Docker
from diagrams.onprem.workflow import Airflow

def create_architecture_diagram():

    # Define the directory and file path
    design_name = "OpsSig Apache Solutions Processings"
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, f"{design_name.lower().replace(' ', '_')}_diagram")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")
    
    with Diagram(f"{design_name} Architecture", direction="LR", show=False, outformat="png", filename=output_file_path):
        # Architecture diagrams
        # Main workflow components
        with Cluster("Company Data Storage"):
            company_storage = Databricks("Feature Data Storage")

        with Cluster("Final Data Storage"):
            opssig_storage = Databricks("OpsSig Delta Tables")
    
        with Cluster("Spark Ecosystem"):
            spark = Spark("Spark Job")
    
        with Cluster("Trino Components"):
            hive_metastore = Hive("Hive Metastore")
            trino_server = Presto("Trino Server")
    
        with Cluster("Superset Analytics"):
            superset = Superset("Superset")
    
        # Monitoring and Orchestration
        with Cluster("Orchestration & Monitoring"):
            airflow = Airflow("Airflow")
            grafana = Grafana("Grafana")
    
        # Optionally include host/container details if using Docker or Linux
        with Cluster("Deployment Environment"):
            docker = Docker("Docker")
    
        trino_server << docker  # Trino runs in Docker

        # Workflow connections
        company_storage >> spark >> opssig_storage  # Spark job writes data to Delta tables
        hive_metastore << Edge(label="Delta Lake Connector") << opssig_storage  # Hive connects to Delta tables
        trino_server << hive_metastore  # Trino reads Hive Metastore
    
        # Connection to Superset
        superset << Edge(label="JDBC/Trino Connector") << trino_server

        # Monitoring and orchestration connections
        airflow >> Edge(label="ETL Orchestration") >> spark
        grafana << Edge(label="Monitoring Metrics") << opssig_storage

if __name__ == "__main__":
    create_architecture_diagram()
