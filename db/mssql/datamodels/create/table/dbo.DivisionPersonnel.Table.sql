USE [C:\USERS\TEPPLER\SOURCE\REPOS\BUDGETPY\DB\MSSQL\DATAMODELS\DATA.MDF]
GO
/****** Object:  Table [dbo].[DivisionPersonnel]    Script Date: 8/21/2021 9:33:33 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[DivisionPersonnel](
	[PersonnelId] [int] NOT NULL,
	[RcCode] [nvarchar](255) NULL,
	[DivisionName] [nvarchar](255) NULL,
	[EmployeeId] [nvarchar](255) NULL,
	[LastName] [nvarchar](255) NULL,
	[FirstName] [nvarchar](255) NULL,
	[JobTitle] [nvarchar](255) NULL,
	[Grade] [nvarchar](255) NULL,
	[Step] [nvarchar](255) NULL,
	[HireDate] [datetime] NULL,
	[LastIncrease] [datetime] NULL,
	[GradeEntry] [datetime] NULL,
	[StepEntry] [datetime] NULL,
	[WigiDueDate] [datetime] NULL,
	[Tenure] [float] NULL,
	[HrOrgName] [nvarchar](255) NULL,
	[Email] [nvarchar](255) NULL,
	[PhoneNumber] [nvarchar](255) NULL,
	[Office] [nvarchar](255) NULL,
	[MailCode] [nvarchar](255) NULL,
	[SupervisorId] [nvarchar](255) NULL,
	[SupervisorFirstName] [nvarchar](255) NULL,
	[SupervisorLastName] [nvarchar](255) NULL,
	[Supervisor] [nvarchar](255) NULL,
 CONSTRAINT [PrimaryKeyDivisionPersonnel] PRIMARY KEY CLUSTERED 
(
	[PersonnelId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
