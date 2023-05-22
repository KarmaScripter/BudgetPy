USE [Data]
GO
/****** Object:  Table [dbo].[ProgramFinancingSchedule]    Script Date: 5/13/2023 1:48:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ProgramFinancingSchedule](
	[ProgramFinancingScheduleId] [int] NOT NULL,
	[ReportYear] [nvarchar](80) NULL,
	[TreasuryAgencyCode] [nvarchar](80) NULL,
	[TreasuryAccountCode] [nvarchar](80) NULL,
	[LedgerAccountCode] [nvarchar](80) NULL,
	[SectionNumber] [nvarchar](80) NULL,
	[SectionName] [nvarchar](80) NULL,
	[LineNumber] [nvarchar](80) NULL,
	[LineDescription] [nvarchar](80) NULL,
	[BudgetAgencyCode] [nvarchar](80) NULL,
	[BudgetAccountCode] [nvarchar](80) NULL,
	[BudgetAccountName] [nvarchar](80) NULL,
	[AgencySequence] [nvarchar](80) NULL,
	[AccountSequence] [nvarchar](80) NULL,
	[FundName] [nvarchar](80) NULL,
	[OriginalAmount] [float] NULL,
	[BudgetAmount] [float] NULL,
	[AgencyAmount] [float] NULL,
	[Amount] [float] NULL,
	[AgencyName] [nvarchar](80) NULL,
 CONSTRAINT [PK_ProgramFinancingSchedule] PRIMARY KEY CLUSTERED 
(
	[ProgramFinancingScheduleId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
