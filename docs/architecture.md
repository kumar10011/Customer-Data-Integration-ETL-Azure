# Architecture and Data Flow

## End-to-end flow

```text
                   +----------------------+
                   | Azure Blob Storage   |
                   | input/               |
                   +----------+-----------+
                              |
                              v
                   +----------------------+
                   | ADF Get Metadata     |
                   +----------+-----------+
                              |
                              v
                   +----------------------+
                   | ForEach File         |
                   +----------+-----------+
                              |
                              v
                   +----------------------+
                   | Lookup MetadataTable |
                   +----------+-----------+
                              |
                     +--------+--------+
                     |                 |
                 configured        not configured
                     |                 |
                     v                 v
             Copy to Bronze       Error Log
                     |
                     v
             +---------------+
             | PySpark Clean |
             +-------+-------+
                     |
                     v
                 Silver
                     |
                     v
             Gold transformation
                     |
                     v
              Azure SQL Customer
```

## Why metadata-driven processing?

Instead of creating a separate hard-coded pipeline for every file type, the pipeline checks the file extension and looks up the destination configuration.

For example:

```text
customers.csv -> customer folder
customers.json -> customer folder
```

This makes the pipeline easier to extend.

## Failure handling

If a file type is not present in `MetadataTable`, the pipeline does not continue the normal copy operation. The file and error message are recorded in `ETLErrorLog`.

## Bronze / Silver / Gold

- Bronze: raw or minimally processed data.
- Silver: cleansed and standardized data.
- Gold: business/reporting-ready data.
