import os
from diagrams import Diagram, Cluster, Edge
# Additinoal Imports
from diagrams.c4 import Person, System, Container, Database

def create_architecture_diagram():

    # Define the directory and file path
    design_name = "E22 Monthly Data Processing"
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, f"{design_name.replace(' ', '_')}_diagram")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")
    
    with Diagram(f"{design_name.title()} Architecture", direction="TB", show=False, outformat="png", filename=output_file_path):
        # Architecture diagrams
        # Define actors and systems
        with Cluster("Databricks Datastore"):
            source_c3 = System("C3 Source System", "Source System 1")
            source_elis = System("ELIS Source System", "Source System 2")
            source_other = System("Other Source System", "Source System 3")
        
            databricks_export = System("Databricks Export Process", "Databricks Data Export")
        
            
        with Cluster("PRT Reporting Tool"):
            external_processing = Container("External Data Processing", "SQL/ETL Tool", "Processes data in custom appliation")
        
        with Cluster("E22 Data Pipeline"):
            ingest_service = Container("Databricks Ingest", "Ingest Process", "Ingests data into Databricks")
            validation_service = Container("Databricks Validation", "Validation Process", "Validates ingested data")
            stage_db = Database("Stage Data", "Staging area for data transformation")
            etl_service = Container("Databricks ETL", "ETL Process", "Transforms and stages data")
        
        with Cluster("E22 Production Push"):
            production_load = Container("Databricks Production Load", "Table Update Process", "Transfers stages data to production")
            prod_db = Database("Production Data", "Published production data")
        
        reporting_system = System("Reporting System", "Tableau / Databricks Dashboard / IMAPS", "Presents aggregated insights")

        # Define relationships
        source_c3 >> databricks_export
        source_elis >> databricks_export
        source_other >> databricks_export
        
        databricks_export >> external_processing
        
        external_processing >> ingest_service
        
        ingest_service >> validation_service
        validation_service >> etl_service
        etl_service >> stage_db
        stage_db >> production_load
        production_load >> prod_db
        prod_db >> reporting_system


if __name__ == "__main__":
    create_architecture_diagram()
