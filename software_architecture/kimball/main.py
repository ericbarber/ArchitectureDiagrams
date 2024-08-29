from diagrams import Diagram, Cluster
from diagrams.aws.storage import S3
from diagrams.generic.database import SQL
from diagrams.onprem.analytics import Tableau
from diagrams.onprem.client import User
import os

def create_kimball_diagram():
# Define the directory and file path
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, "kimball_diagram")

# Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")

    with Diagram("Kimball Data Flow", direction="TB", show=False, outformat="png", filename=output_file_path):
        sources = [S3("ERP System"), S3("CRM System"), S3("Legacy System")]

        
        with Cluster("Data Marts"):
            sales_dm = SQL("Sales Data Mart")
            finance_dm = SQL("Finance Data Mart")
            inventory_dm = SQL("Inventory Data Mart")
        
        dw = SQL("Integrated Data Warehouse")

        user = User("Business User")
        
        for source in sources:
            source >> [sales_dm, inventory_dm, finance_dm] >> dw
        
        dw >> Tableau("Reports") >> user

if __name__ == "__main__":
    create_kimball_diagram()
