CREATE TABLE [dbo].[Book]
(
	[Id] INT NOT NULL PRIMARY KEY,
	[Title] VARCHAR(MAX) NOT NULL,
	[Description] VARCHAR(MAX) NULL,
	[ISBN] INT NOT NULL, --Candidate Key
)
