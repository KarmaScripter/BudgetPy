USE [Data]
GO
/****** Object:  Table [dbo].[GeneralLedgerAccounts]    Script Date: 5/13/2023 1:48:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[GeneralLedgerAccounts](
	[GeneralLedgerAccountsId] [int] NOT NULL,
	[BFY] [nvarchar](80) NULL,
	[Number] [nvarchar](80) NULL,
	[Name] [nvarchar](80) NULL,
	[ShortName] [nvarchar](80) NULL,
	[AccountClassification] [nvarchar](80) NULL,
	[NormalBalance] [nvarchar](80) NULL,
	[RealOrClosingAccount] [nvarchar](80) NULL,
	[CashAccount] [nvarchar](80) NULL,
	[SummaryAccount] [nvarchar](80) NULL,
	[ReportableAccount] [nvarchar](80) NULL,
	[CostAllocationIndicator] [nvarchar](80) NULL,
	[FederalNonFederal] [nvarchar](80) NULL,
	[AttributeValue] [nvarchar](80) NULL,
	[Usage] [nvarchar](80) NULL,
	[Deposit] [nvarchar](80) NULL,
 CONSTRAINT [PK_GeneralLedgerAccounts] PRIMARY KEY CLUSTERED 
(
	[GeneralLedgerAccountsId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
