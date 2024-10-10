from diagrams import Cluster, Diagram, Edge
from diagrams.aws.analytics import Redshift
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS, DynamodbTable
from diagrams.aws.integration import SNS
from diagrams.onprem.analytics import Databricks
import os
# Additinoal Imports

def create_architecture_diagram():

    # Define the directory and file path
    design_name = "signal watch"
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, f"{design_name.replace(' ', '_')}_diagram")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")
    
    with Diagram(f"{design_name.title()} Architecture", direction="LR", show=False, outformat="png", filename=output_file_path):
        
        with Cluster("SignalWatch"):
            # Architecture diagrams

            # Step 1: Feature query from datastore
            datastore = RDS("Datastore")
            query = Databricks("Feature Query")

            model = EC2("Feature Model")
            datastore >> query >> model

            # Step 2: Feature model and control analysis
            with Cluster("Continuous Process Monitoring"):
                analysis = Databricks("Control Analysis")
                alerts_table = DynamodbTable("Alert Processing")

                query >> Edge(label="Direct Analysis", style="dashed") >> analysis >> alerts_table
                model >> analysis

                # Step 3: Notification of anomalous events
                sms_notification = SNS("SMS Notification")

                alerts_table >> sms_notification

if __name__ == "__main__":
    create_architecture_diagram()
