USE [Data]
GO
/****** Object:  Table [dbo].[AdministrativeRequests]    Script Date: 5/13/2023 1:48:16 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AdministrativeRequests](
	[AdministrativeRequestsId] [int] NOT NULL,
	[RequestId] [float] NULL,
	[Analyst] [nvarchar](80) NULL,
	[RpioCode] [nvarchar](80) NULL,
	[DocumentTitle] [nvarchar](80) NULL,
	[Amount] [float] NULL,
	[FundCode] [nvarchar](80) NULL,
	[BFY] [nvarchar](80) NULL,
	[Status] [nvarchar](80) NULL,
	[OriginalRequestDate] [datetime] NULL,
	[LastActivityDate] [datetime] NULL,
	[Duration] [float] NULL,
	[BudgetFormulationSystem] [nvarchar](80) NULL,
	[Comments] [nvarchar](max) NULL,
	[RequestDocument] [nvarchar](max) NULL,
	[RequestType] [nvarchar](80) NULL,
	[TypeCode] [nvarchar](80) NULL,
	[Decision] [nvarchar](80) NULL,
 CONSTRAINT [PK_AdministrativeRequests] PRIMARY KEY CLUSTERED 
(
	[AdministrativeRequestsId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
