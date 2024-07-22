CREATE TABLE [dbo].[Author]
(
	[Id] INT NOT NULL PRIMARY KEY IDENTITY, 
    [FirstName] NVARCHAR(50) NOT NULL, 
    [LastName] NVARCHAR(50) NOT NULL, 
    [OtherNames] NVARCHAR(100) NULL, 
    [Bio] TEXT NULL
)
