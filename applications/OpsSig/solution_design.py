import os
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.analytics import Superset, Hive, Presto, Spark, Databricks
from diagrams.onprem.workflow import Airflow
from diagrams.onprem.container import Docker
from diagrams.onprem.monitoring import Grafana

def create_architecture_diagram():

    design_name = "OpsSig Data Architecture"
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, f"{design_name.lower().replace(' ', '_')}_diagram")

    # Create output directory if not exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")
    
    with Diagram(f"{design_name} Architecture", direction="LR", show=False, outformat="png", filename=output_file_path):
        
        # 1. Data Ingestion & Storage
        with Cluster("Data Ingestion & Storage"):
            company_storage = Databricks("Feature Data Storage")

        # 2. Data Processing & Transformation
        with Cluster("Data Processing & Transformation"):
            spark = Spark("Spark Job")
            airflow = Airflow("Airflow Orchestration")

        # 3. Data Storage & Metadata Management
        with Cluster("Data Storage & Metadata"):
            opssig_storage = Databricks("OpsSig Delta Tables")
            hive_metastore = Hive("Hive Metastore")

        # 4. Data Querying & Analytics
        with Cluster("Data Querying & Analytics"):
            trino_server = Presto("Trino Server")
            superset = Superset("Superset")

        # 5. Deployment & Monitoring Environment
        with Cluster("Deployment & Monitoring"):
            docker = Docker("Docker")
            grafana = Grafana("Grafana")

        # Define workflow connections
        # Data flow through the pipeline
        company_storage >> Edge(label="Ingest Data") >> spark >> Edge(label="Process Data") >> opssig_storage
        opssig_storage >> Edge(label="Delta Lake Connector") >> hive_metastore
        hive_metastore >> Edge(label="Hive Metastore") >> trino_server
        trino_server >> Edge(label="JDBC/Trino Connector") >> superset

        # Monitoring and orchestration
        airflow >> Edge(label="Orchestrates") >> spark
        grafana << Edge(label="Monitors Metrics") << opssig_storage

        # Docker deployment
        docker >> Edge(label="Containerized Services") >> trino_server

if __name__ == "__main__":
    create_architecture_diagram()
