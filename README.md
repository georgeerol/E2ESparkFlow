# E2E Spark Flow
This project handles data from start to finish using Docker, Apache Airflow, Kafka, Spark, Cassandra, and PostgreSQL. 
These tools work together to take in, handle, and keep data.

# System Architecture
![System Architecture](./SparkFlowArchitecture.png)


# Technologies
1. **Apache Airflow**: An open-source platform used to programmatically author, schedule, and monitor workflows. Supports Python for workflow authoring.
2. **Apache Kafka**: An open-source distributed streaming platform for fault tolerance, high throughput, and a publish-subscribe messaging system.
3. **Apache Spark**: An open-source, powerful processing engine capable of handling intensive big data workloads. Its ability to perform batch processing, stream processing, and machine learning makes it an excellent tool for all data processing needs.
4. **Apache Cassandra**: An open-source NoSQL database, excellent for handling large amounts of write-heavy data. Its distributed design offers high availability without compromising fault tolerance, crucial for systems requiring uninterrupted operation.
5. **PostgreSQL**: An open-source relational database, in this case, focused on saving Airflow metadata.
6. **Docker**: An open-source containerization tool allowing isolated, consistent, and accessible deployment. Containers ensure consistency across multiple development, testing, and production environments, reducing the “it works on my machine” problem.
7. **Apache Zookeeper**: An open-source centralized service for maintaining configuration information, naming, and providing distributed synchronization. Essential for managing clustered services like Kafka.


---

# Starting the Project with Docker Compose

Docker Compose is a tool for defining and running multi-container Docker applications. For this project, It will orchestrate the containers for Apache Airflow, Kafka, Spark, Cassandra, PostgreSQL, and any other required services.

## Prerequisites

- Docker and Docker Compose installed on your system.

## Steps to Start the Project

1. **Clone the Project Repository (if not already done):**
   - Use Git to clone the project repository to your local machine.
   - Navigate to the root directory of the project.

2. **Configure Docker Compose:**
   - Ensure you have the `docker-compose.yml` file in your project directory. This file defines the configuration for each service (Airflow, Kafka, Spark, etc.).

3. **Building and Starting Containers:**
   - Open a Terminal/Command Prompt.
   - Navigate to your project directory.
   - Run the following command to build and start the containers as defined in your Docker Compose file:

     ```bash
     docker-compose up --build
     ```

   - This command builds the images for your services (if not already built) and starts the containers.

4. **Verify the Services:**
   - Once the containers run, you can verify that each service functions correctly.
   - You can access the web interfaces of services, like Apache Airflow, through your web browser.

5. **Stopping the Services:**
   - To stop and remove the containers, use the following command in the same directory:

     ```bash
     docker-compose down
     ```

   - This command stops all the running containers and removes them and their networks.
