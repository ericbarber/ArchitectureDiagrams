import os
from diagrams import Diagram, Cluster
# Additinoal Imports

def create_architecture_diagram():

    # Define the directory and file path
    design_name = ""
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, f"{design_name.replace(' ', '_')}_diagram")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")
    
    with Diagram(f"{design_name.title()} Architecture", direction="LR", show=False, outformat="png", filename=output_file_path):
        # Architecture diagrams


if __name__ == "__main__":
    create_architecture_diagram()
