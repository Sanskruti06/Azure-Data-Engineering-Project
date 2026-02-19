**Azure End-to-End Data Engineering Project**

**Project Overview**

This project demonstrates a complete Azure-based data engineering pipeline implementing the Medallion Architecture (Bronze → Silver → Gold).

The solution ingests raw data from Github URL, stores it in Azure Data Lake Storage Gen2, processes it using Azure Databricks (PySpark), and exposes curated datasets through Azure Synapse Analytics for analytics and reporting.

(Original Dataset Link: https://www.kaggle.com/datasets/ukveteran/adventure-works)

This project simulates a real-world enterprise data engineering workflow.

---

**Architecture Diagram**
<img width="1536" height="1024" alt="Architecture" src="https://github.com/user-attachments/assets/592fe245-fb45-4edc-ac21-eb0b1c392c7c" />

End-to-End Data Flow

**1. Data Ingestion (Bronze Layer)**
- Azure Data Factory pipelines ingest CSV data from Github.
- Raw data is stored in Azure Data Lake Storage Gen2 (Bronze container).
- Dynamic pipelines implemented using Lookup + ForEach activities.

  <img width="2936" height="1544" alt="image" src="https://github.com/user-attachments/assets/af4a28f9-e68c-41f8-b627-b32cc20b308f" />


  <img width="2938" height="1544" alt="image" src="https://github.com/user-attachments/assets/4fbb5eb6-db16-4738-88f0-09ed82128bea" />



**2. Data Transformation (Silver Layer)**
- Azure Databricks notebooks process raw data.
- Data cleaning, transformation, and schema enforcement performed using PySpark.
- Data stored in Parquet format for optimized querying.

<img width="2938" height="1592" alt="image" src="https://github.com/user-attachments/assets/1ed51632-d1cb-4630-a690-4fe4e3cf92b2" />


<img width="2938" height="1540" alt="image" src="https://github.com/user-attachments/assets/abd7e93f-3d24-4db0-bc58-87e0bab9fd08" />



**3. Data Serving (Gold Layer)**
- Aggregated datasets created.
- Azure Synapse Serverless SQL used to:
  - Create external tables
  - Run OPENROWSET queries
  - Create views for reporting

<img width="2938" height="1546" alt="image" src="https://github.com/user-attachments/assets/24dc1c22-3ed5-488e-9e57-397d69362f11" />


<img width="2936" height="1540" alt="image" src="https://github.com/user-attachments/assets/de363408-96a1-4f22-8b8d-897fe1e5affe" />



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
