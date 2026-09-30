CREATE TABLE dbo.Customer
(
    CustomerID INT NOT NULL PRIMARY KEY,
    CustomerName VARCHAR(200) NOT NULL,
    Email VARCHAR(320) NOT NULL,
    Phone VARCHAR(30) NOT NULL,
    City VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    ProcessedTimestamp DATETIME2 NULL
);
