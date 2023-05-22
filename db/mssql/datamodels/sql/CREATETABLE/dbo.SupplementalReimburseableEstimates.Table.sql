USE [Data]
GO
/****** Object:  Table [dbo].[SupplementalReimburseableEstimates]    Script Date: 5/13/2023 1:48:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SupplementalReimburseableEstimates](
	[ReimbursableEstimatesId] [int] NULL,
	[BFY] [nvarchar](80) NULL,
	[EFY] [nvarchar](80) NULL,
	[FundCode] [nvarchar](80) NULL,
	[FundName] [nvarchar](80) NULL,
	[RpioCode] [nvarchar](80) NULL,
	[RpioName] [nvarchar](80) NULL,
	[Amount] [float] NULL,
	[OpenCommitments] [float] NULL,
	[Obligations] [float] NULL,
	[Available] [float] NULL,
	[Estimate] [float] NULL
) ON [PRIMARY]
GO
