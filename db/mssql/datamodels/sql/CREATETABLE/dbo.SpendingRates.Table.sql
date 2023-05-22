USE [Data]
GO
/****** Object:  Table [dbo].[SpendingRates]    Script Date: 5/13/2023 1:48:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SpendingRates](
	[SpendingRatesId] [int] NOT NULL,
	[OmbAgencyCode] [nvarchar](80) NULL,
	[OmbAgencyName] [nvarchar](80) NULL,
	[OmbBureauCode] [nvarchar](80) NULL,
	[OmbBureauName] [nvarchar](80) NULL,
	[TreausuryAgencyCode] [nvarchar](80) NULL,
	[TreausuryAccountCode] [nvarchar](80) NULL,
	[TreausuryAccountName] [nvarchar](80) NULL,
	[AccountTitle] [nvarchar](80) NULL,
	[Subfunction] [nvarchar](80) NULL,
	[Line] [nvarchar](80) NULL,
	[LineNumber] [nvarchar](80) NULL,
	[Category] [nvarchar](80) NULL,
	[Subcategory] [nvarchar](80) NULL,
	[SubcategoryName] [nvarchar](80) NULL,
	[MainAccount] [nvarchar](80) NULL,
	[Jurisdiction] [nvarchar](80) NULL,
	[YearOfAuthority] [nvarchar](80) NULL,
	[BudgetAuthority] [float] NULL,
	[OutYear1] [float] NULL,
	[OutYear2] [float] NULL,
	[OutYear3] [float] NULL,
	[OutYear4] [float] NULL,
	[OutYear5] [float] NULL,
	[OutYear6] [float] NULL,
	[OutYear7] [float] NULL,
	[OutYear8] [float] NULL,
	[OutYear9] [float] NULL,
	[OutYear10] [float] NULL,
	[OutYear11] [float] NULL,
	[TotalSpendout] [float] NULL,
 CONSTRAINT [PK_SpendingRates] PRIMARY KEY CLUSTERED 
(
	[SpendingRatesId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
