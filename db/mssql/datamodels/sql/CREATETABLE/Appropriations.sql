CREATE TABLE [dbo].[Appropriations]
(
	[AppropriationId] [int] IDENTITY(1,1) NOT NULL,
	[BFY] [nvarchar](255) NOT NULL,
	[Title] [nvarchar](255) NULL,
	[PublicLaw] [nvarchar](255) NULL,
	[EnactedDate] [datetime] NULL
);
