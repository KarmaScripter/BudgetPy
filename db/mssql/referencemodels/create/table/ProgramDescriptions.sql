CREATE TABLE [dbo].[ProgramDescriptions]
(
	[ProgramProjectId] [int] IDENTITY(1,1) NOT NULL,
	[ProgramProjectCode] [nvarchar](255) NOT NULL,
	[ProgramProjectName] [nvarchar](255) NULL,
	[ProgramProjectTitle] [nvarchar](255) NULL,
	[Laws] [nvarchar](max) NULL,
	[Narrative] [nvarchar](max) NULL,
	[Definition] [nvarchar](max) NULL,
	[ProgramAreaCode] [nvarchar](255) NULL,
	[ProgramAreaName] [nvarchar](255) NULL
);
