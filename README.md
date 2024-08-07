# Precision RAG: Prompt Tuning For Building Enterprise RAG Systems

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [Key Features](#key-features) 
- [License](#license)

## Project Overview

The project involves collaborating with a city traffic department to collect traffic data using swarm UAVs (drones) from multiple locations. The goal is to build a salable data warehouse capable of hosting vehicle trajectory data extracted from drone footage and roadside cameras.
This warehouse will be designed to accommodate future needs and enable efficient querying for downstream projects.


## Setup Instructions

### Prerequisites

- Python 3.x
- NodeJS 18
- yarn 1.22.22
- docker 

### Installation

1. **Clone the Repository**
   ```sh
   git clone git@github.com:jadmassu/open_traffic_data_warehouse.git
   cd open_traffic_data_warehouse
   ```

2. **Install Requirements**

   ```sh
   pip install -r requirements.txt
   ```

3. **Run airflow**
   ```sh
   cd airflow
   docker-compose up 
   ```

**Run Next Application**

```sh
cd redash
make build
make compose_build
make up
```

**Open with your browser to see the result.**

[http://localhost:3000](http://localhost:5001)

## Project Structure

    ├── airflow                 # Contains files and directories for Airflow setup and workflows
    │   ├── dags                # Directory for Directed Acyclic Graphs (DAGs) defining workflows
    │   ├── models              # Directory for data models used within Airflow
    │   ├── utils               # Utility scripts and helpers for Airflow
    │   ├── docker-compose.yaml # Docker Compose configuration for setting up Airflow environment
    │   ├── requirements.txt    # List of Python dependencies for Airflow
    │   └── ...                 # Other Airflow-related files and directories
    ├── dbt                     # Contains files and directories for DBT (Data Build Tool)
    │   ├── models              # Directory for DBT models defining data transformations
    │   └── ...                 # Other DBT-related files and directories
    ├── logs                    # Directory for storing log files generated by the system
    ├── redash                  # Directory for Redash configuration and resources
    ├── README.md               # Project documentation and setup instructions
    └── ...                     # Other project-related files and directories


## Key Features

* Dynamic Task Scheduling: Allows the creation of complex workflows with dependencies and scheduling.
* Bash and Python Operators: Facilitates running scripts and custom Python code for data loading and processing.
* SQL-based Modeling: Simplifies writing transformations using SQL, making it accessible for analysts and engineers.
* Real-time Analytics: Connects to the data warehouse to provide up-to-date dashboards and visualizations.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
