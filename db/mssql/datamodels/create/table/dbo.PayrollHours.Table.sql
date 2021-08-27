USE [C:\USERS\TEPPLER\SOURCE\REPOS\BUDGETPY\DB\MSSQL\DATAMODELS\DATA.MDF]
GO
/****** Object:  Table [dbo].[PayrollHours]    Script Date: 8/21/2021 9:33:33 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PayrollHours](
	[PayrollHoursId] [int] NOT NULL,
	[RpioCode] [nvarchar](255) NULL,
	[PayPeriod] [nvarchar](255) NULL,
	[StartDate] [datetime] NULL,
	[EndDate] [datetime] NULL,
	[EpaNumber] [nvarchar](255) NULL,
	[FirstName] [nvarchar](255) NULL,
	[LastName] [nvarchar](255) NULL,
	[HrOrgCode] [nvarchar](255) NULL,
	[HrOrgName] [nvarchar](255) NULL,
	[ReportingCode] [nvarchar](255) NULL,
	[ReportingCodeName] [nvarchar](255) NULL,
	[WorkCode] [nvarchar](255) NULL,
	[Hours] [float] NULL,
 CONSTRAINT [PrimaryKeyPayrollHours] PRIMARY KEY CLUSTERED 
(
	[PayrollHoursId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
