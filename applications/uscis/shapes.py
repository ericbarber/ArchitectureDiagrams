
import os
from diagrams import Diagram, Cluster, Edge
# Additinoal Imports
from diagrams.programming.flowchart import StartEnd, Action, Decision, ManualInput, StoredData
from diagrams.onprem.vcs import Git
from diagrams.onprem.client import Users


def create_architecture_diagram():

    # Define the directory and file path
    design_name = "New Git Actions for Shapes Clone 001"
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, f"{design_name.replace(' ', '_')}_diagram")
    print(output_file_path)

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")
    
    with Diagram(f"{design_name.title()} Architecture", direction="TB", show=False, outformat="png", filename=output_file_path):
        # Architecture diagrams
        # Elements
        start_pull = StartEnd("Start Pull")
        end_pull = StartEnd("End Pull")

        start_push = StartEnd("Start Push")
        end_push = StartEnd("End Push")
        

        with Cluster("User Interface"):
        
            user = Users("User")
        
            # Git Repository and Actions
            with Cluster("Git Repository Directory"):
                git_repo = Git("Git Repository")

                with Cluster("Git Operations"):
                    pull_changes = Action("Pull Latest Changes")
                    push_changes = Action("Push Latest Changes")
        

            with Cluster("Git Bash Terminal"):
                push_or_pull = Decision("Push Or Pull Operations?")

            # Workflow
            user >> git_repo
            git_repo >> push_or_pull
      
        # Tableau Directory and Shapes Folder
        with Cluster("Tableau Directory"):
            shapes_dir = StoredData("Shapes Directory")

        # Pull
        with Cluster("Pull Operations"):
            create_backup = Decision("Create Backup (Optional)")
            prompt_overwrite = ManualInput("Prompt User Overwrite? (Optional)")
            copy_files = Action("Copy Files to Shapes Dir")
            
            push_or_pull >> Edge(label="Pull") >> pull_changes >> start_pull
            check_shapes_dir = Decision("Shapes Directory Exists?")
            # Branch for directory existence
            start_pull >> check_shapes_dir >> Edge(label="Yes") >> create_backup
            create_backup >> prompt_overwrite
            prompt_overwrite >> copy_files
            # Interaction with the Shapes Directory
            check_shapes_dir >> Edge(label="No") >> shapes_dir
            create_backup >> shapes_dir
            copy_files >> shapes_dir >> end_pull
        
        # Push 
        push_or_pull >> Edge(label="Push") >> push_changes >> start_push
        start_push >> end_push

if __name__ == "__main__":
    create_architecture_diagram()
