# E2E Spark Flow
This project handles data from start to finish using Docker, Apache Airflow, Kafka, Spark, Cassandra, and PostgreSQL. 
These tools work together to take in, handle, and keep data.

# System Architecture
![System Architecture](./SparkFlowArchitecture.png)


# Technologies
1. **Apache Airflow**is a platform for programmatically authoring, scheduling, and monitoring workflows. It allows you to organize and manage tasks efficiently.
2. **Python**: A popular programming language known for its readability and versatility. It's widely used for web development, data analysis, artificial intelligence, and scientific computing.
3. **Apache Kafka**: A distributed streaming platform. It's used for building real-time data pipelines and streaming apps. It can handle high-throughput data feeds.
4. **Apache Zookeeper**: A centralized service for maintaining configuration information, naming, distributed synchronization, and group services, it's often used in distributed systems to manage their services.
5. **Apache Spark**: An open-source, distributed processing system for big data workloads. It provides development APIs in Python, Java, Scala, and R, and an optimized engine that supports general computation graphs.
6. ** Cassandra ** is a distributed NoSQL database designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure.
7. **PostgreSQL**: A powerful, open-source object-relational database system. It uses and extends the SQL language with many features that safely store and scale complicated data workloads.
8. **Docker**: A platform for developing, shipping, and running applications. It enables you to separate your applications from your infrastructure to quickly deliver software. Docker packages software into standardized units called containers with everything the software needs to run, including libraries, system tools, code, and runtime.

Certainly! Here's an additional section on how to start the project using Docker Compose, which can be added to your existing documentation:

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
   - Once the containers are up and running, you can verify that each service functions correctly.
   - You can access the web interfaces of services like Apache Airflow, through your web browser.

5. **Stopping the Services:**
   - To stop and remove the containers, use the following command in the same directory:

     ```bash
     docker-compose down
     ```

   - This command stops all the running containers and removes them and their networks.
