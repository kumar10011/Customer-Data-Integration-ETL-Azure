CREATE TABLE dbo.ETLErrorLog
(
    ErrorID INT IDENTITY(1,1) PRIMARY KEY,
    FileName VARCHAR(255),
    ErrorMessage VARCHAR(1000),
    ErrorDateTime DATETIME2 NOT NULL DEFAULT SYSDATETIME()
);

GO

CREATE PROCEDURE dbo.LogETLError
    @FileName VARCHAR(255),
    @ErrorMessage VARCHAR(1000)
AS
BEGIN
    INSERT INTO dbo.ETLErrorLog(FileName, ErrorMessage)
    VALUES(@FileName, @ErrorMessage);
END;
GO
