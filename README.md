# Customer Data Integration and ETL Pipeline on Azure

## Project Overview

This project demonstrates a batch ETL pipeline built using Azure Data Factory (ADF), Azure Blob Storage, PySpark and Azure SQL Database.

Customer source files are received in Azure Blob Storage. ADF orchestrates ingestion and movement through the ETL stages, while PySpark is used for data cleansing and standardization. The final curated customer data is loaded into Azure SQL Database for reporting and analytics.

## Architecture

```text
Azure Blob Storage
      |
      |  CSV / JSON / XML / TXT
      v
+-----------------------+
| Azure Data Factory    |
| Master Pipeline       |
+-----------------------+
      |
      v
Source -> Bronze
      |
      v
Bronze -> Silver
      |       (PySpark cleansing)
      v
Silver -> Gold
      |
      v
Azure SQL Database
      |
      v
Reporting / Analytics
```

## Pipeline Design

The project uses a master/child pipeline pattern:

1. `MasterPipeline` orchestrates the ETL stages.
2. `SourceToBronze` ingests source files into the raw/bronze layer.
3. `BronzeToSilver` applies cleansing and standardization logic.
4. `SilverToGold` applies business-ready transformations.
5. `GoldToAzureSQL` loads the final customer dataset into Azure SQL Database.

A metadata/configuration table is used to determine the destination folder based on the source file type.

## Key ADF Activities

- Get Metadata
- ForEach
- Lookup
- If Condition
- Copy Data
- Execute Pipeline
- Stored Procedure
- Set Variable

## Example Dynamic File Processing

ADF Get Metadata returns `childItems`. The ForEach activity iterates through the files:

```text
@activity('GetMetadata1').output.childItems
```

The current file name is obtained using:

```text
@item().name
```

The file extension is derived using:

```text
@last(split(item().name,'.'))
```

The configuration table can then be queried to determine the destination folder.

Example Lookup query:

```sql
SELECT FolderName
FROM MetadataTable
WHERE FileType = '@{last(split(item().name,'.'))}'
```

The destination folder can be referenced with:

```text
@activity('Lookup1').output.firstRow.FolderName
```

## Data Quality Rules

The PySpark transformation performs common data-quality operations:

- Trim whitespace
- Standardize customer names
- Convert email addresses to lowercase
- Handle null values
- Standardize phone values
- Remove duplicate customer records
- Validate customer IDs
- Add processing timestamp

## Example Source

```text
CustomerID,CustomerName,Email,Phone,City,Country
1001, Anjani Kumar ,ANJANI@EXAMPLE.COM,9876543210,Hyderabad,India
1002,Ravi Kumar,,9123456780,Chennai,India
1002,Ravi Kumar,ravi@example.com,9123456780,Chennai,India
1003, Priya Sharma ,PRIYA@EXAMPLE.COM,,Bengaluru,India
```

## Expected Transformation

```text
Raw data
   |
   +-- trim customer name
   +-- lowercase email
   +-- fill missing values
   +-- standardize phone
   +-- remove duplicate CustomerID
   |
   v
Clean customer data
```

## Azure Services

| Service | Purpose |
|---|---|
| Azure Blob Storage | Source file storage |
| Azure Data Factory | ETL orchestration |
| PySpark | Data cleansing and transformation |
| Azure SQL Database | Curated destination |
| Azure Key Vault / Managed Identity | Secret management in a production implementation |

## Repository Structure

```text
Customer-Data-Integration-ETL-Azure/
|
+-- ADF/
|   +-- pipeline/
|   +-- dataset/
|   +-- linkedService/
|   +-- dataflow/
|   +-- trigger/
|
+-- PySpark/
|   +-- customer_cleaning.py
|   +-- customer_gold.py
|
+-- SQL/
|   +-- 01_metadata_table.sql
|   +-- 02_error_table.sql
|   +-- 03_customer_table.sql
|   +-- 04_sample_queries.sql
|
+-- SampleData/
|   +-- customers.csv
|
+-- docs/
|   +-- architecture.md
|
+-- README.md
+-- .gitignore
```

## Security

No passwords, access keys, connection strings or secrets are stored in this repository.

Linked-service files contain placeholders only. In Azure, credentials should be handled through Managed Identity, Azure Key Vault or secure integration mechanisms.

## Important Note

The JSON files in this repository are documentation/repository versions of the ADF artifacts. Environment-specific connection information and secrets are intentionally excluded.

## Interview Summary

A concise explanation of the project:

> "I built a customer data integration ETL pipeline using Azure Data Factory. Customer files were received in Azure Blob Storage. ADF handled orchestration using Get Metadata, ForEach, Lookup, Copy Data and Execute Pipeline activities. The data was processed through bronze, silver and gold stages. PySpark was used for cleansing, null handling, standardization and duplicate removal. Finally, the curated customer data was loaded into Azure SQL Database for reporting and analytics. I also used metadata-driven file routing so the pipeline could process different file types without hard-coding every file path."
