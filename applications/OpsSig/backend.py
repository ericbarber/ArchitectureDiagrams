import os
from diagrams import Diagram, Cluster, Edge
# Additinoal Imports
from diagrams.c4 import Person, Container, Database, SystemBoundary, Relationship

# C4 diagram attributes
graph_attr = {
    "splines": "spline",
    "fontcolor": "black",  # Set font color to black
}

node_attr = {
    "fontcolor": "black",  # Set the text color inside shapes to black
}

def create_architecture_diagram():

    # Define the directory and file path
    design_name = "OpsSig Backend"
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, f"{design_name.replace(' ', '_')}_diagram")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")
    
    with Diagram(
        f"{design_name} Architecture",
        direction="LR",
        show=False,
        graph_attr=graph_attr,
        node_attr=node_attr,
        outformat="png",
        filename=output_file_path):
        # Architecture diagrams
        # Define entities as C4 Containers and Databases
        departments = Database(
            name="Departments Table",
            technology="Delta Table",
            description="Stores department details such as name, lead info, and point of contact."
        )
    
        features = Database(
            name="Features Table",
            technology="Delta Table",
            description="Stores information about features associated with departments."
        )
    
        controls = Database(
            name="Controls Table",
            technology="Delta Table",
            description="Stores control configurations linked to features."
        )
    
        control_runs = Database(
            name="Control Runs Table",
            technology="Delta Table",
            description="Tracks control run data for features, including control signals."
        )
    
        notifications = Database(
            name="Notifications Table",
            technology="Delta Table",
            description="Stores notification details related to controls."
        )
    
        notification_runs = Database(
            name="Notification Runs Table",
            technology="Delta Table",
            description="Tracks runs of notifications sent for controls."
        )
    
        # Define relationships
        departments >> Relationship("linked by department_id") >> [features, controls]
        features >> Relationship("linked by feature_id") >> controls
        controls >> Relationship("linked by control_id") >> [control_runs, notifications]
        control_runs >> Relationship("linked by control_run_id") >> notification_runs
        notifications >> Relationship("linked by notification_id") >> notification_runs
        notifications >> Relationship("linked by control_id") >> notification_runs
if __name__ == "__main__":
    create_architecture_diagram()
