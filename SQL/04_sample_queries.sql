-- Count records loaded
SELECT COUNT(*) AS CustomerCount
FROM dbo.Customer;

-- Check duplicate CustomerID
SELECT CustomerID, COUNT(*) AS RecordCount
FROM dbo.Customer
GROUP BY CustomerID
HAVING COUNT(*) > 1;

-- Check nulls in important columns
SELECT
    SUM(CASE WHEN CustomerName IS NULL THEN 1 ELSE 0 END) AS NullCustomerName,
    SUM(CASE WHEN Email IS NULL THEN 1 ELSE 0 END) AS NullEmail,
    SUM(CASE WHEN City IS NULL THEN 1 ELSE 0 END) AS NullCity
FROM dbo.Customer;
