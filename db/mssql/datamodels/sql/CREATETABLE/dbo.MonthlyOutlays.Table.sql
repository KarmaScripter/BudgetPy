USE [Data]
GO
/****** Object:  Table [dbo].[MonthlyOutlays]    Script Date: 5/13/2023 1:48:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[MonthlyOutlays](
	[MonthlyOutlaysId] [int] NOT NULL,
	[FiscalYear] [nvarchar](80) NULL,
	[LineNumber] [nvarchar](80) NULL,
	[LineTitle] [nvarchar](80) NULL,
	[TaxationCode] [nvarchar](80) NULL,
	[TreasuryAgencyCode] [nvarchar](80) NULL,
	[TreasuryAccountCode] [nvarchar](80) NULL,
	[SubAccount] [nvarchar](80) NULL,
	[BFY] [nvarchar](80) NULL,
	[EFY] [nvarchar](80) NULL,
	[BudgetAgencyCode] [nvarchar](80) NULL,
	[BudgetBureauCode] [nvarchar](80) NULL,
	[BudgetAccountCode] [nvarchar](80) NULL,
	[AgencySequence] [nvarchar](80) NULL,
	[BureauSequence] [nvarchar](80) NULL,
	[AccountSequence] [nvarchar](80) NULL,
	[AgencyTitle] [nvarchar](80) NULL,
	[BureauTitle] [nvarchar](80) NULL,
	[BudgetAccountName] [nvarchar](80) NULL,
	[TreasuryAccountName] [nvarchar](80) NULL,
	[October] [float] NULL,
	[November] [float] NULL,
	[December] [float] NULL,
	[January] [float] NULL,
	[Feburary] [float] NULL,
	[March] [float] NULL,
	[April] [float] NULL,
	[May] [float] NULL,
	[June] [float] NULL,
	[July] [float] NULL,
	[August] [float] NULL,
	[September] [float] NULL,
 CONSTRAINT [PK_MonthlyOutlays] PRIMARY KEY CLUSTERED 
(
	[MonthlyOutlaysId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
