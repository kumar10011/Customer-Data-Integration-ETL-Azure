CREATE TABLE dbo.MetadataTable
(
    MetadataID INT IDENTITY(1,1) PRIMARY KEY,
    FileType VARCHAR(20) NOT NULL,
    FolderName VARCHAR(100) NOT NULL,
    IsActive BIT NOT NULL DEFAULT 1,
    CreatedDate DATETIME2 NOT NULL DEFAULT SYSDATETIME()
);

INSERT INTO dbo.MetadataTable (FileType, FolderName, IsActive)
VALUES
('csv', 'customer', 1),
('json', 'customer', 1),
('xml', 'customer', 1),
('txt', 'customer', 1);
