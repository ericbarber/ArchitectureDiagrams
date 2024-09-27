import os
from diagrams import Diagram, Cluster
from diagrams.k8s.compute import Pod, StatefulSet
from diagrams.k8s.network import Service, Ingress
from diagrams.k8s.storage import PersistentVolume, PersistentVolumeClaim
from diagrams.k8s.group import Namespace
from diagrams.k8s.podconfig import ConfigMap, Secret
# Additinoal Imports

def create_architecture_diagram():

    # Define the diand file path
    design_name = "k8s"
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, f"{design_name.replace(' ', '_')}_diagram")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")
    
    with Diagram(f"{design_name.title()} Architecture", direction="TB", show=False, outformat="png", filename=output_file_path):
        # Architecture diagrams
        with Cluster("Airflow"):
            airflow_web = Pod("airflow-web")
            airflow_scheduler = StatefulSet("airflow-scheduler")
            airflow_postgres = Pod("postgres")
            airflow_service = Service("airflow-web-svc")

            # Storage for Airflow
            airflow_pv = PersistentVolume("airflow-pv")
            airflow_pvc = PersistentVolumeClaim("airflow-pvc")

        with Cluster("Delta Table (Spark)"):
            spark_master = Pod("spark-master")
            spark_worker = Pod("spark-worker")
            spark_service = Service("spark-master-svc")

            # Storage for Spark
            spark_pv = PersistentVolume("spark-pv")
            spark_pvc = PersistentVolumeClaim("spark-pvc")

        # Kubernetes components
        namespace = Namespace("helm-namespace")
        helm_config = ConfigMap("helm-config")
        helm_secrets = Secret("helm-secrets")

        # Ingress to expose services
        ingress = Ingress("ingress")

        # Relationships
        airflow_web >> airflow_service
        airflow_scheduler >> airflow_postgres
        airflow_web >> airflow_pv
        airflow_service >> ingress

        spark_master >> spark_service
        spark_worker >> spark_pv
        spark_service >> ingress


if __name__ == "__main__":
    create_architecture_diagram()
