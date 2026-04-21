CREATE TABLE [dbo].[BookAuthor]
(
	[Id] INT NOT NULL PRIMARY KEY,
	BookId INT NOT NULL, --Foreign Key
	AuthorId INT NOT NULL, --Foreign Key
	CONSTRAINT FK_BookAuthor_Book FOREIGN KEY (BookId) REFERENCES Book(Id),
	CONSTRAINT FK_BookAuthor_Author FOREIGN KEY (AuthorId) REFERENCES Author(Id)
)
