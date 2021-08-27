USE [C:\USERS\TEPPLER\SOURCE\REPOS\BUDGETPY\DB\MSSQL\DATAMODELS\DATA.MDF]
GO
/****** Object:  Table [dbo].[Supplemental]    Script Date: 8/21/2021 9:33:33 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Supplemental](
	[SupplementalId] [float] NOT NULL,
	[Type] [nvarchar](255) NULL,
	[RcCode] [nvarchar](255) NULL,
	[FundCode] [nvarchar](255) NULL,
	[BFY] [nvarchar](255) NULL,
	[BocCode] [nvarchar](255) NULL,
	[BocName] [nvarchar](255) NULL,
	[Amount] [float] NULL,
	[Time] [float] NULL,
 CONSTRAINT [PrimaryKeySupplemental] PRIMARY KEY CLUSTERED 
(
	[SupplementalId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
