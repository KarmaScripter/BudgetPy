CREATE TABLE [dbo].[Documents]
(
	[DocumentId] [int] IDENTITY(1,1) NOT NULL,
	[Code] [nvarchar](255) NULL,
	[Category] [nvarchar](255) NULL,
	[Name] [nvarchar](255) NULL,
	[System] [nvarchar](255) NULL
);
