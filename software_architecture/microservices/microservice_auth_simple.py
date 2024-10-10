
import os
from diagrams import Diagram, Cluster
# Additinoal Imports
from diagrams.c4 import Person, Container, Relationship

def create_architecture_diagram():

    # Define the directory and file path
    design_name = "microservice auth and gateway"
    output_directory = "./diagrams"
    output_file_path = os.path.join(output_directory, f"{design_name.replace(' ', '_')}_diagram")

    # Check if the directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")
    
    with Diagram(f"{design_name.title()} Architecture", direction="LR", show=False, outformat="png", filename=output_file_path):
        # Architecture diagrams
        # People
        user = Person(name="User", description="End user interacting with the application")
        
        # Microservices (Containers)
        with Cluster("Client") as client: 
            web_app = Container(
                name="Web App", 
                technology="React, Node.js", 
                description="Frontend service for user interaction"
            )

        api_gateway = Container(
            name="API Gateway", 
            technology="Express.js", 
            description="Entry point for API requests"
        )
        auth_service = Container(
            name="Auth Service", 
            technology="Python, Flask", 
            description="Handles authentication and authorization"
        )
        order_service = Container(
            name="Order Service", 
            technology="Java, Spring Boot", 
            description="Manages order processing"
        )
        payment_service = Container(
            name="Payment Service", 
            technology="Go", 
            description="Handles payment transactions"
        )
        db = Container(
            name="Database", 
            technology="PostgreSQL", 
            description="Stores application data"
        )
    
        # Relationships
        user >> Relationship("uses") >> web_app
        web_app >> Relationship("calls") >> api_gateway
        api_gateway >> Relationship("authenticates with") >> auth_service
        api_gateway >> Relationship("sends order to") >> order_service
        order_service >> Relationship("requests payment from") >> payment_service
        order_service >> Relationship("stores/queries data") >> db
        payment_service >> Relationship("stores/queries payment info") >> db

if __name__ == "__main__":
    create_architecture_diagram()
