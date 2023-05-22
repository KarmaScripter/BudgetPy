USE [Data]
GO
/****** Object:  Table [dbo].[GrossUtilization]    Script Date: 5/13/2023 1:48:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[GrossUtilization](
	[GrossUtilizationId] [int] NOT NULL,
	[BFY] [nvarchar](80) NULL,
	[EFY] [nvarchar](80) NULL,
	[FundCode] [nvarchar](80) NULL,
	[FundName] [nvarchar](80) NULL,
	[RpioCode] [nvarchar](80) NULL,
	[RpioName] [nvarchar](80) NULL,
	[AhCode] [nvarchar](80) NULL,
	[AhName] [nvarchar](80) NULL,
	[OrgCode] [nvarchar](80) NULL,
	[OrgName] [nvarchar](80) NULL,
	[AccountCode] [nvarchar](80) NULL,
	[ProgramProjectName] [nvarchar](80) NULL,
	[BocCode] [nvarchar](80) NULL,
	[BocName] [nvarchar](80) NULL,
	[Committed] [nvarchar](80) NULL,
	[Obligated] [nvarchar](80) NULL,
	[Unliquidated] [nvarchar](80) NULL,
	[Utilization] [nvarchar](80) NULL,
	[Availability] [nvarchar](80) NULL,
	[Outlaid] [nvarchar](80) NULL,
 CONSTRAINT [PK_GrossUtilization] PRIMARY KEY CLUSTERED 
(
	[GrossUtilizationId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
