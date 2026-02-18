**Azure End-to-End Data Engineering Project**

**Project Overview**

This project demonstrates a complete Azure-based data engineering pipeline implementing the Medallion Architecture (Bronze → Silver → Gold).

The solution ingests raw data from GitHub, stores it in Azure Data Lake Storage Gen2, processes it using Azure Databricks (PySpark), and exposes curated datasets through Azure Synapse Analytics for analytics and reporting.

This project simulates a real-world enterprise data engineering workflow.

---

**Architecture Diagram**
<img width="1536" height="1024" alt="Architecture" src="https://github.com/user-attachments/assets/592fe245-fb45-4edc-ac21-eb0b1c392c7c" />

End-to-End Data Flow

**1. Data Ingestion (Bronze Layer)**
- Azure Data Factory pipelines ingest CSV data from GitH₹ub.
- Raw data is stored in Azure Data Lake Storage Gen2 (Bronze container).
- Dynamic pipelines implemented using Lookup + ForEach activities.
  
  <img width="2936" height="1594" alt="image" src="https://github.com/user-attachments/assets/3cbdf7f8-de0e-4ea7-9942-11376f7f8fab" />


**2. Data Transformation (Silver Layer)**
- Azure Databricks notebooks process raw data.
- Data cleaning, transformation, and schema enforcement performed using PySpark.
- Data stored in Parquet format for optimized querying.

<img width="2938" height="1594" alt="image" src="https://github.com/user-attachments/assets/96d36b32-e866-4424-bee4-f223752fca99" />


**3. Data Serving (Gold Layer)**
- Aggregated datasets created.
- Azure Synapse Serverless SQL used to:
  - Create external tables
  - Run OPENROWSET queries
  - Create views for reporting

<img width="2938" height="1202" alt="image" src="https://github.com/user-attachments/assets/e2f5fb81-c302-42a6-a755-088ba1360d53" />


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
