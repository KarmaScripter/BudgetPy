USE [C:\USERS\TEPPLER\SOURCE\REPOS\BUDGETPY\DB\MSSQL\DATAMODELS\DATA.MDF]
GO
/****** Object:  Table [dbo].[EmployeeLeave]    Script Date: 8/21/2021 9:33:33 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[EmployeeLeave](
	[EmployeeLeaveId] [int] NOT NULL,
	[RcCode] [nvarchar](255) NULL,
	[LastName] [nvarchar](255) NULL,
	[FirstName] [nvarchar](255) NULL,
	[EpaNumber] [nvarchar](255) NULL,
	[HoursEarnedYearToDate] [float] NULL,
	[CarryoverHours] [float] NULL,
	[HoursAdjustedYearToDate] [float] NULL,
	[HoursBalance] [float] NULL,
	[ProjectedAnnualHours] [float] NULL,
	[ProjectedNextPeriodHours] [float] NULL,
	[HoursTakenYearToDate] [float] NULL
) ON [PRIMARY]
GO
