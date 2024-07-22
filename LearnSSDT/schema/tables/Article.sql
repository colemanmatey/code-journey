CREATE TABLE [dbo].[Article]
(
	[Id] INT NOT NULL PRIMARY KEY IDENTITY, 
    [Title] VARCHAR(50) NULL, 
    [Content] TEXT NULL, 
    [AuthorID] INT NOT NULL, 
    CONSTRAINT [FK_Article_Author] FOREIGN KEY (AuthorID) REFERENCES [Author]([Id])
)
