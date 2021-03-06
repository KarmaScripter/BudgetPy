CREATE TABLE [dbo].[Allocations]
(
	[PrcId] [int] IDENTITY(1,1) NOT NULL,
	[BudgetLevel] [nvarchar](50) NOT NULL,
	[RPIO] [nvarchar](50) NOT NULL,
	[BFY] [nvarchar](50) NOT NULL,
	[FundCode] [nvarchar](50) NOT NULL,
	[AhCode] [nvarchar](50) NOT NULL,
	[OrgCode] [nvarchar](50) NOT NULL,
	[RcCode] [nvarchar](50) NOT NULL,
	[AccountCode] [nvarchar](50) NOT NULL,
	[BocCode] [nvarchar](50) NOT NULL,
	[Amount] [float] NOT NULL,
	[ActivityCode] [nvarchar](50) NOT NULL,
	[ActivityName] [nvarchar](50) NOT NULL,
	[FundName] [nvarchar](50) NOT NULL,
	[BocName] [nvarchar](50) NOT NULL,
	[NpmName] [nvarchar](50) NOT NULL,
	[Division] [nvarchar](50) NOT NULL,
	[DivisionName] [nvarchar](50) NOT NULL,
	[ProgramProjectCode] [nvarchar](50) NOT NULL,
	[ProgramProjectName] [nvarchar](100) NOT NULL,
	[ProgramAreaName] [nvarchar](50) NOT NULL,
	[AhName] [nvarchar](50) NOT NULL,
	[OrgName] [nvarchar](50) NOT NULL,
	[GoalName] [nvarchar](50) NOT NULL,
	[ObjectiveName] [nvarchar](50) NOT NULL
);
