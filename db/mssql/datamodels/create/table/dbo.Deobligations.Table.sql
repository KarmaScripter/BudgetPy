USE [C:\USERS\TEPPLER\SOURCE\REPOS\BUDGETPY\DB\MSSQL\DATAMODELS\DATA.MDF]
GO
/****** Object:  Table [dbo].[Deobligations]    Script Date: 8/21/2021 9:33:33 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Deobligations](
	[DeobligationId] [int] NOT NULL,
	[RPIO] [nvarchar](255) NULL,
	[BFY] [nvarchar](255) NULL,
	[FundCode] [nvarchar](255) NULL,
	[DocumentNumber] [nvarchar](255) NULL,
	[CalendarYear] [nvarchar](255) NULL,
	[OrgCode] [nvarchar](255) NULL,
	[ProgramProjectCode] [nvarchar](255) NULL,
	[AccountCode] [nvarchar](255) NULL,
	[BocCode] [nvarchar](255) NULL,
	[Date] [datetime] NULL,
	[Amount] [float] NULL,
 CONSTRAINT [PrimaryKeyDeobligations] PRIMARY KEY CLUSTERED 
(
	[DeobligationId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
