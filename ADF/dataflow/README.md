# Data transformation layer

The project uses PySpark for the main customer cleansing logic. If an ADF Mapping Data Flow is used in an Azure implementation, the equivalent transformations can be represented here.

Typical transformation sequence:

```text
Source
  -> Derived Column
  -> Filter invalid records
  -> Aggregate / Deduplicate
  -> Select
  -> Sink
```

The repository keeps the main transformation implementation in `PySpark/customer_cleaning.py` so the logic can also be tested outside ADF.
