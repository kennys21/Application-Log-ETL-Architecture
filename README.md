<a id="readme-top"></a>

# Cloud Log Ingestion and Transformation Pipeline

A cloud-based batch log ingestion and transformation pipeline built using AWS and Python.  
This project simulates application log ingestion, validation, cleaning, and loading into a relational database for analytical querying.

This repository represents a foundational step in my data engineering learning journey, focusing on building structured ETL pipelines and layered data architecture.

---

## About The Project

This project demonstrates how semi-structured log data can be:

- Generated (simulating application events)
- Stored in a raw format
- Parsed and validated
- Cleaned and transformed
- Loaded into AWS RDS
- Queried using SQL for analytics

The goal is to design and implement a structured batch ETL pipeline using cloud infrastructure while applying data engineering best practices such as schema enforcement, deduplication, and layered architecture.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Architecture Overview

Pipeline flow:

1. Log generation (Python)
2. Raw data storage
3. Parsing and validation
4. Data transformation
5. Load into AWS RDS
6. Analytical SQL queries

Data layers:

Raw Layer  
Logs stored as generated, including malformed and incomplete records.

Staging Layer  
Logs parsed into structured format with validation applied.

Processed Layer  
Cleaned, normalized, and deduplicated data stored in RDS for analysis.

---

## Built With

- Python
- AWS EC2
- AWS RDS
- PostgreSQL



---

## Dataset

Logs are generated using a custom Python script that simulates application events.

To approximate real-world conditions, the generator intentionally introduces:

- Missing fields
- Corrupted timestamps
- Mixed log levels (INFO, WARNING, ERROR)
- Duplicate records
- Malformed log entries

This ensures the transformation layer must handle:

- Null value handling
- Timestamp normalization
- Deduplication
- Schema enforcement
- Invalid record filtering

Although synthetic, the dataset is intentionally imperfect to simulate real ingestion challenges.

---

## ETL Process

Extract  
Logs are generated and written to the raw layer.

Transform  
Python scripts parse log lines, validate structure, normalize timestamps, remove duplicates, and enforce schema consistency.

Load  
Cleaned records are inserted into AWS RDS using parameterized SQL queries.

---

## Example Analytical Queries

- Count of logs by level
- Error frequency by service
- Logs aggregated by hour
- Detection of abnormal error spikes



### Prerequisites

- Python 3.x
- AWS account
- EC2 instance configured
- RDS instance configured
- Database credentials set

---

## Limitations

- Batch processing only
- Manual execution (no scheduler)
- No S3 data lake layer
- No orchestration framework
- No containerization
- Synthetic data source

This project focuses on foundational pipeline architecture rather than production-grade deployment.

---

## Future Improvements

- Introduce S3 as raw data storage
- Add workflow orchestration (e.g., Airflow)
- Containerize using Docker
- Implement table partitioning
- Add automated data quality checks
- Introduce streaming ingestion (Kafka or Kinesis)
- Add CI/CD integration

---

## Learning Objectives

Through this project i mainly practiced:

- Designing layered data pipelines
- Handling semi-structured log data
- Writing ETL validation logic
- Designing relational schemas
- Deploying compute and storage in AWS
- Structuring a repository using engineering best practices

---

## Contact

Your Name  
GitHub: https://github.com/kennys21


Project Link:  
https://github.com/kennys21/Application-Log-Architecture

<p align="right">(<a href="#readme-top">back to top</a>)</p>
