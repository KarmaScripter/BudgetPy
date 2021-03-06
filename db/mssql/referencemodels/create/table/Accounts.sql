CREATE TABLE [dbo].[Accounts]
(
	[AccountCodeId] [int] IDENTITY(1,1) NOT NULL,
	[Code] [nvarchar](255) NULL,
	[ProgramProjectCode] [nvarchar](255) NULL,
	[ProgramProjectName] [nvarchar](255) NULL,
	[ProgramAreaCode] [nvarchar](255) NULL,
	[ProgramAreaName] [nvarchar](255) NULL,
	[GoalCode] [nvarchar](max) NULL,
	[ObjectiveCode] [nvarchar](max) NULL,
	[NpmCode] [nvarchar](max) NULL
);
