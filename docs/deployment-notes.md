# Deployment Notes

1. Create Azure Blob Storage containers: `input`, `bronze`, `silver`, `gold`.
2. Create Azure SQL Database.
3. Execute SQL scripts in order:
   - 01_metadata_table.sql
   - 02_error_table.sql
   - 03_customer_table.sql
4. Create ADF.
5. Create linked services using Managed Identity or Key Vault-backed secrets.
6. Create datasets and pipelines from the repository artifacts.
7. Configure the Databricks/PySpark environment if using Databricks.
8. Parameterize environment-specific paths.
9. Run `MasterPipeline`.
10. Validate the target table and ADF Monitor output.

Do not put real connection strings or secrets into GitHub.
