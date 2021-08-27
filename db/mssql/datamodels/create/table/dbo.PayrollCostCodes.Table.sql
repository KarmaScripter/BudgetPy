USE [C:\USERS\TEPPLER\SOURCE\REPOS\BUDGETPY\DB\MSSQL\DATAMODELS\DATA.MDF]
GO
/****** Object:  Table [dbo].[PayrollCostCodes]    Script Date: 8/21/2021 9:33:33 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PayrollCostCodes](
	[PayrollCostCodeId] [int] NOT NULL,
	[RcCode] [nvarchar](255) NULL,
	[DivisionName] [nvarchar](255) NULL,
	[HrOrgCode] [nvarchar](255) NULL,
	[HrOrgName] [nvarchar](255) NULL,
	[WorkCode] [nvarchar](255) NULL,
	[WorkCodeName] [nvarchar](255) NULL,
 CONSTRAINT [PrimaryKeyPayrollCostCodes] PRIMARY KEY CLUSTERED 
(
	[PayrollCostCodeId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
