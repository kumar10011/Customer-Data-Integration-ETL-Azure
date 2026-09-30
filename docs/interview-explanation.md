# Interview Explanation

## 60-second explanation

"I worked on a customer data integration ETL pipeline using Azure Data Factory. Customer files were placed in Azure Blob Storage. ADF was used as the orchestration layer. I used Get Metadata to identify files, ForEach to process them, Lookup to read configuration from a metadata table, and Copy activities to move data through the pipeline. The data was organized into bronze, silver and gold stages. PySpark handled cleansing, null handling, formatting and duplicate removal. The final curated data was loaded into Azure SQL Database for reporting."

## If asked why ADF?

"ADF is primarily an orchestration and data integration service. I used it to connect the source and target systems, control the sequence of activities, pass parameters, handle dynamic files and monitor pipeline execution."

## If asked where PySpark was used

"ADF handled orchestration, while PySpark handled transformation logic such as trimming, standardization, null handling and deduplication."

## If asked about GitHub

"The repository contains the project artifacts and transformation code. Environment-specific secrets and connection details are intentionally excluded. In a real Azure environment, the ADF artifacts can be managed through source control and deployed between environments."

## If asked whether this is executable directly from GitHub

"The repository is a source-control representation of the project. Azure-specific resources such as the storage account, ADF instance, SQL database and credentials must exist in the target Azure environment before deployment."
