USE [C:\USERS\TEPPLER\SOURCE\REPOS\BUDGETPY\DB\MSSQL\DATAMODELS\DATA.MDF]
GO
/****** Object:  Table [dbo].[SiteSpending]    Script Date: 8/21/2021 9:33:33 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SiteSpending](
	[SiteSpendingId] [int] NOT NULL,
	[BFY] [nvarchar](255) NULL,
	[AhCode] [nvarchar](255) NULL,
	[FundCode] [nvarchar](255) NULL,
	[FundName] [nvarchar](255) NULL,
	[AccountCode] [nvarchar](255) NULL,
	[ProgramProjectName] [nvarchar](255) NULL,
	[BocCode] [nvarchar](255) NULL,
	[BocName] [nvarchar](255) NULL,
	[RcCode] [nvarchar](255) NULL,
	[DivisionName] [nvarchar](255) NULL,
	[OrgCode] [nvarchar](255) NULL,
	[OrgName] [nvarchar](255) NULL,
	[FocCode] [nvarchar](255) NULL,
	[FocName] [nvarchar](255) NULL,
	[SiteProjectCode] [nvarchar](255) NULL,
	[SiteProjectName] [nvarchar](255) NULL,
	[SSID] [nvarchar](255) NULL,
	[SiteActionCode] [nvarchar](255) NULL,
	[SiteOperableUnit] [nvarchar](255) NULL,
	[EpaSiteId] [nvarchar](255) NULL,
	[City] [nvarchar](255) NULL,
	[State] [nvarchar](255) NULL,
	[VendorCode] [nvarchar](255) NULL,
	[VendorName] [nvarchar](255) NULL,
	[DocumentType] [nvarchar](255) NULL,
	[DocumentControlNumber] [nvarchar](255) NULL,
	[Requested] [float] NULL,
	[Closed] [float] NULL,
	[Outstanding] [float] NULL,
	[Reversed] [float] NULL,
	[Refunded] [float] NULL,
 CONSTRAINT [PrimaryKeySiteSpending] PRIMARY KEY CLUSTERED 
(
	[SiteSpendingId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
