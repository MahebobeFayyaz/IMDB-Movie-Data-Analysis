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

* Load IMDB movie data into S3.
  <img width="940" height="386" alt="image" src="https://github.com/user-attachments/assets/ec96bbf8-ad3b-4c6b-869e-3a28810fb085" />

* Use AWS Glue to create a Data Catalog Crawler for the data in S3.
  <img width="940" height="420" alt="image" src="https://github.com/user-attachments/assets/5d18c845-9856-452e-a2a5-11aa7a3ca75b" />
  <img width="940" height="502" alt="image" src="https://github.com/user-attachments/assets/b6d52012-6bab-4411-8919-5788930d6e8e" />


* Apply Glue Data Quality Rules to validate the source data.
  <img width="940" height="471" alt="image" src="https://github.com/user-attachments/assets/56478974-35f2-4b80-ae29-e82a9cf6a543" />

* Outcomes of the rules are written to another S3 bucket for analysis.
  <img width="940" height="355" alt="image" src="https://github.com/user-attachments/assets/349e8090-3d7f-4023-997e-6276a48d39c6" />

* Set up a Redshift cluster as the destination for the processed data.
* <img width="940" height="441" alt="image" src="https://github.com/user-attachments/assets/3c09b3c7-3440-4674-bd56-3a733e610c71" />

* Create a Schema for the Destination table.
* Create a Glue Crawler to catalog the Redshift destination table.
  <img width="940" height="418" alt="image" src="https://github.com/user-attachments/assets/6e55f00a-d45e-4bfb-a33d-59d397224829" />

* Implement an ETL workflow in AWS Glue:
* Transform the data:
* Route failed records to an S3 bucket for further analysis using Athena and Quicksight.
* Route passed records to the Redshift destination.
* Configure Amazon EventBridge and SNS for notifications on ETL success or failure.
