USE [C:\USERS\TEPPLER\SOURCE\REPOS\BUDGETPY\DB\MSSQL\DATAMODELS\DATA.MDF]
GO
/****** Object:  Table [dbo].[PurchaseRequestNumbers]    Script Date: 8/21/2021 9:33:33 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PurchaseRequestNumbers](
	[PurchaseRequestId] [int] NOT NULL,
	[RcCode] [nvarchar](255) NULL,
	[PurchaseRequest] [nvarchar](255) NULL,
 CONSTRAINT [PrimaryKeyPurchaseRequestNumbers] PRIMARY KEY CLUSTERED 
(
	[PurchaseRequestId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
