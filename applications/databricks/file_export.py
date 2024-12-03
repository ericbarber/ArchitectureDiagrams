import os
from diagrams import Diagram, Cluster
# Additinoal Imports
from diagrams.onprem.client import User
from diagrams.aws.storage import ElasticFileSystemEFSFileSystem
from diagrams.programming.language import Python
from diagrams.generic.storage import Storage

def create_architecture_diagram():

    # Define the directory and file path
    design_name = "Databricks File Export Import"
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, f"{design_name.replace(' ', '_')}_diagram")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")
    
    with Diagram(f"{design_name.title()} Architecture", direction="LR", show=False, outformat="png", filename=output_file_path):
        # Architecture diagrams
        # User icon
        user = User("You")
    
        # Databricks Workspace
        with Cluster("Databricks Workspace"):
            workspace = ElasticFileSystemEFSFileSystem("Workspace\n(notebooks, metadata)")
        
        # DBFS
        with Cluster("Databricks File System (DBFS)"):
            dbfs = Storage("dbfs:/")
        
        # Local Temporary Directory
        with Cluster("Local Temp Directory"):
            local_tmp = Storage("Local Temp\n(/tmp or custom path)")
        
        # # File operations
        # export_operation = Python("Export\nworkspace_api.export_workspace")
        # copy_operation = Python("Copy\ndbutils.fs.cp")
        # read_write_operation = Python("Read/Write\nopen()")
        
        # Connections
        # user >> workspace >> export_operation >> local_tmp
        # local_tmp >> read_write_operation
        # local_tmp >> copy_operation >> dbfs
        # dbfs >> read_write_operation

        import_function = Python("Import\n(import_to_workspace)")
        save_function = Python("Save\n(save_to_dbfs)")
        export_function = Python("Export\n(workspace_api.export_workspace)")
        read_write_function = Python("Read/Write\nopen()")

        # Workflow connections
        user >> workspace >> export_function >> local_tmp
        local_tmp >> read_write_function
        local_tmp >> save_function >> dbfs
        local_tmp >> import_function
        dbfs >> import_function >> workspace


if __name__ == "__main__":
    create_architecture_diagram()
