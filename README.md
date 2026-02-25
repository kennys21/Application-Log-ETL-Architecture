Cloud Log Ingestion and Transformation Pipeline
Overview

This project demonstrates a cloud-based batch log ingestion and transformation pipeline built using AWS infrastructure and Python.

The goal of this project is to simulate how application logs are ingested, validated, cleaned, transformed, and stored in a relational database for analytical querying.

This project is part of my data engineering learning journey and focuses on building foundational pipeline architecture using EC2, RDS, Python, and SQL.

Architecture

High-level pipeline flow:

Log generation (simulated application logs)

Raw log storage

Parsing and validation (Python)

Data cleaning and transformation

Load into AWS RDS

Analytical querying

Conceptual layers:

Raw layer
Logs are stored as generated, including malformed or incomplete records.

Staging layer
Logs are parsed into structured format with schema enforcement. Invalid or corrupted records are filtered or flagged.

Processed layer
Cleaned, normalized, and deduplicated data is stored in AWS RDS for querying.

Tech Stack

##Python (data generation, parsing, transformation)

#AWS EC2 (compute environment)

##AWS RDS (relational database)

##PostgreSQL

Dataset

Logs are generated using a Python script to simulate application events.

To better approximate real-world conditions, the generator intentionally introduces:

Missing fields

Corrupted timestamps

Mixed log levels (INFO, ERROR, WARNING)

Duplicate records

Malformed log lines
PostgreSQL or MySQL

SQL
