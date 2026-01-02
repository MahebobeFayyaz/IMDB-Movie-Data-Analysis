# IMDB Movie Data End-to-End Pipeline
An end-to-end pipeline for processing IMDB movie data using AWS services.

# Project Overview
Project Overview This project demonstrates an end-to-end data pipeline built on AWS for processing and analyzing IMDB movie data. The pipeline is designed to automate data ingestion, quality checks, transformation, and loading into a Redshift data warehouse for further analysis. Notifications are sent at various stages of the pipeline for monitoring and alerting.

# Architecture
The architecture leverages the following AWS services:
* S3: For storing raw, intermediate, and processed data.
* AWS Glue: For building the data catalog, running ETL jobs, and implementing data quality checks.
* AWS Redshift: As the final destination for processed data.
* Athena & Quicksight: For querying and visualizing failed transformation records.
* Amazon EventBridge: For scheduling and monitoring ETL jobs.
* Amazon SNS: For sending success and failure notifications.

# Pipeline Workflow

<img width="688" height="647" alt="388178759-c81ae5a9-16bb-40a8-91f8-39e0f2ac622f" src="https://github.com/user-attachments/assets/703b5d99-8cb7-42ef-b7de-3db4a9fbd427" />
