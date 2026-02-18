**Azure End-to-End Data Engineering Project**

**Project Overview**

This project demonstrates a complete Azure-based data engineering pipeline implementing the Medallion Architecture (Bronze → Silver → Gold).

The solution ingests raw data from GitHub, stores it in Azure Data Lake Storage Gen2, processes it using Azure Databricks (PySpark), and exposes curated datasets through Azure Synapse Analytics for analytics and reporting.

This project simulates a real-world enterprise data engineering workflow.

---

End-to-End Data Flow

**1. Data Ingestion (Bronze Layer)**
- Azure Data Factory pipelines ingest CSV data from GitH₹ub.
- Raw data is stored in Azure Data Lake Storage Gen2 (Bronze container).
- Dynamic pipelines implemented using Lookup + ForEach activities.

**2. Data Transformation (Silver Layer)**
- Azure Databricks notebooks process raw data.
- Data cleaning, transformation, and schema enforcement performed using PySpark.
- Data stored in Parquet format for optimized querying.

**3. Data Serving (Gold Layer)**
- Aggregated datasets created.
- Azure Synapse Serverless SQL used to:
  - Create external tables
  - Run OPENROWSET queries
  - Create views for reporting

**4. Analytics Layer**
- The curated Gold layer data is exposed through Azure Synapse Serverless SQL and is ready for consumption by BI tools such as Power BI.


**5. Future Enhancements**
How to Integrate Power BI
	1.	Open Power BI Desktop
	2.	Click Get Data → Azure → Azure Synapse Analytics (SQL Server)
	3.	Enter Synapse Serverless endpoint
	4.	Select Gold layer views
	5.	Build dashboards using measures and visuals
	6.	Publish report to Power BI Service

---

**Technologies Used**

- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks
- Azure Synapse Analytics (Serverless SQL)
- PySpark
- SQL
- Parquet
