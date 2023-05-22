USE [Data]
GO
/****** Object:  Table [dbo].[ExecutionTables]    Script Date: 5/13/2023 1:48:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ExecutionTables](
	[ExecutionTablesId] [int] NOT NULL,
	[TableName] [nvarchar](80) NULL,
	[Type] [nvarchar](max) NULL,
 CONSTRAINT [PK_ExecutionTables] PRIMARY KEY CLUSTERED 
(
	[ExecutionTablesId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
