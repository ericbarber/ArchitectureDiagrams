from diagrams import Diagram, Cluster
from diagrams.aws.storage import S3
from diagrams.generic.database import SQL
from diagrams.onprem.analytics import Tableau
from diagrams.onprem.client import User
import os

def create_inmon_diagram():
    # Define the directory and file path
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, "inmon_diagram")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")

    with Diagram("Inmon Data Flow", direction="TB", show=False, outformat="png", filename=output_file_path):
        sources = [S3("CRM System"), S3("Legacy System"), S3("ERP System")]

        with Cluster("Enterprise Data Warehouse (EDW)"):
            edw = SQL("Normalized Data Model")
        
        with Cluster("Data Marts"):
            sales_dm = SQL("Sales Data Mart")
            finance_dm = SQL("Finance Data Mart")
            inventory_dm = SQL("Inventory Data Mart")
        
        user = User("Business User")

        # Data sources feed into the EDW
        for source in sources:
            source >> edw
        
        # EDW feeds into the data marts
        edw >> [sales_dm, inventory_dm, finance_dm]
        
        # Data marts feed reports to the business user
        [sales_dm, inventory_dm, finance_dm] >> Tableau("Reports") >> user

if __name__ == "__main__":
    create_inmon_diagram()

