import os
from diagrams import Diagram, Cluster
from diagrams.onprem.database import Cassandra
from diagrams.generic.database import SQL
# Additinoal Imports

def create_architecture_diagram():

    # Define the directory and file path
    design_name = "data mesh"
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, f"{design_name.replace(' ','_')}_diagram")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")
    
    with Diagram(f"{design_name.title()} Architecture", direction="LR", show=False, outformat="png", filename=output_file_path):
        # Architecture diagrams
        with Cluster("Domain 1"):
            db1 = Cassandra("Domain Database 1")
            product1 = SQL("Data Product 1")

        with Cluster("Domain 2"):
            db2 = Cassandra("Domain Database 2")
            product2 = SQL("Data Product 2")
        
        with Cluster("Central Platform"):
            infra = SQL("Data Infrastructure")

        db1 >> product1 >> infra
        db2 >> product2 >> infra

if __name__ == "__main__":
    create_architecture_diagram()
