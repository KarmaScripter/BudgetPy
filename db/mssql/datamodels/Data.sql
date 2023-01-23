USE [Data]
GO
/****** Object:  Table [dbo].[Allocations]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Allocations](
	[PrcId] [int] IDENTITY(1,1) NOT NULL,
	[BudgetLevel] [nvarchar](50) NULL DEFAULT ('NS'),
	[RPIO] [nvarchar](50) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](50) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](50) NULL DEFAULT ('NS'),
	[AhCode] [nvarchar](50) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](50) NULL DEFAULT ('NS'),
	[RcCode] [nvarchar](50) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](50) NULL DEFAULT ('NS'),
	[BocCode] [nvarchar](50) NULL DEFAULT ('NS'),
	[Amount] [float] NULL DEFAULT (0.0),
	[ActivityCode] [nvarchar](50) NULL DEFAULT ('NS'),
	[ActivityName] [nvarchar](50) NULL DEFAULT ('NS'),
	[FundName] [nvarchar](50) NULL DEFAULT ('NS'),
	[BocName] [nvarchar](50) NULL DEFAULT ('NS'),
	[NpmName] [nvarchar](50) NULL DEFAULT ('NS'),
	[Division] [nvarchar](50) NULL DEFAULT ('NS'),
	[DivisionName] [nvarchar](50) NULL DEFAULT ('NS'),
	[ProgramProjectCode] [nvarchar](50) NULL DEFAULT ('NS'),
	[ProgramProjectName] [nvarchar](100) NOT NULL,
	[ProgramAreaName] [nvarchar](50) NULL DEFAULT ('NS'),
	[AhName] [nvarchar](50) NULL DEFAULT ('NS'),
	[OrgName] [nvarchar](50) NULL DEFAULT ('NS'),
	[GoalName] [nvarchar](50) NULL DEFAULT ('NS'),
	[ObjectiveName] [nvarchar](50) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ApplicationTables]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ApplicationTables](
	[ApplicationTableId] [int] IDENTITY(1,1) NOT NULL,
	[TableName] [nvarchar](80) NULL DEFAULT ('NS'),
	[Model] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AppropriationDocuments]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AppropriationDocuments](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[BFY] [nvarchar](50) NULL DEFAULT ('NS'),
	[EFY] [nvarchar](50) NULL DEFAULT ('NS'),
	[Fund] [nvarchar](50) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](50) NULL DEFAULT ('NS'),
	[DocumentType] [nvarchar](50) NULL DEFAULT ('NS'),
	[DocumentNumber] [nvarchar](50) NULL DEFAULT ('NS'),
	[DocumentDate] [datetime] NOT NULL,
	[LastDocumentDate] [datetime] NOT NULL,
	[BudgetLevel] [nvarchar](50) NULL DEFAULT ('NS'),
	[BudgetingControls] [nvarchar](50) NULL DEFAULT ('NS'),
	[PostingControls] [nvarchar](50) NULL DEFAULT ('NS'),
	[PreCommitmentControls] [nvarchar](50) NULL DEFAULT ('NS'),
	[CommitmentControls] [nvarchar](50) NULL DEFAULT ('NS'),
	[ObligationControls] [nvarchar](50) NULL DEFAULT ('NS'),
	[AccrualControls] [nvarchar](50) NULL DEFAULT ('NS'),
	[ExpenditureControls] [nvarchar](50) NULL DEFAULT ('NS'),
	[ExpenseControls] [nvarchar](50) NULL DEFAULT ('NS'),
	[ReimbursementControls] [nvarchar](50) NULL DEFAULT ('NS'),
	[ReimbursableAgreementControls] [nvarchar](50) NULL DEFAULT ('NS'),
	[Budgeted] [float] NULL DEFAULT (0.0),
	[Posted] [float] NULL DEFAULT (0.0),
	[CarryOut] [float] NULL DEFAULT (0.0),
	[CarryIn] [float] NULL DEFAULT (0.0),
	[EstimatedReimbursements] [float] NULL DEFAULT (0.0),
	[EstimatedRecoveries] [float] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BackUp]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BackUp](
	[BackupAllocationId] [int] IDENTITY(1,1) NOT NULL,
	[PrcId] [float] NULL DEFAULT (0.0),
	[BudgetLevel] [nvarchar](80) NULL DEFAULT ('NS'),
	[RPIO] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[Amount] [float] NULL DEFAULT (0.0),
	[AllocationRatio] [float] NULL DEFAULT (0.0),
	[FundName] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[Division] [nvarchar](80) NULL DEFAULT ('NS'),
	[DivisionName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ActivityCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmName] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaName] [nvarchar](80) NULL DEFAULT ('NS'),
	[GoalCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[GoalName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ObjectiveCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ObjectiveName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ChangeDate] [datetime] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BudgetControlValues]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BudgetControlValues](
	[ControlValueId] [int] IDENTITY(1,1) NOT NULL,
	[Code] [nvarchar](50) NULL DEFAULT ('NS'),
	[Name] [nvarchar](50) NULL DEFAULT ('NS'),
	[SecOrg] [nvarchar](50) NULL DEFAULT ('NS'),
	[BdgtTransType] [nvarchar](50) NULL DEFAULT ('NS'),
	[PstdTransType] [nvarchar](50) NULL DEFAULT ('NS'),
	[EstReimTransType] [nvarchar](50) NULL DEFAULT ('NS'),
	[SpngAdjTransType] [nvarchar](50) NULL,
	[EstRecTransType] [nvarchar](50) NULL DEFAULT ('NS'),
	[ActlRecTransType] [nvarchar](50) NULL,
	[StatRsrvTransType] [nvarchar](50) NULL DEFAULT ('NS'),
	[ProfLossTransType] [nvarchar](50) NULL DEFAULT ('NS'),
	[EstReimSpngOpt] [nvarchar](50) NULL DEFAULT ('NS'),
	[EstReimBdgtOpt] [nvarchar](50) NULL DEFAULT ('NS'),
	[TrckAgreLowerLevel] [nvarchar](50) NULL DEFAULT ('NS'),
	[BdgtEstLowerLevel] [nvarchar](50) NULL DEFAULT ('NS'),
	[EstRecSpngOpt] [nvarchar](50) NULL DEFAULT ('NS'),
	[EstRecBdgtOpt] [nvarchar](50) NULL DEFAULT ('NS'),
	[RecNextLevel] [nvarchar](50) NULL DEFAULT ('NS'),
	[RecBdgtMismatch] [nvarchar](50) NULL DEFAULT ('NS'),
	[ProfitLossSpngOpt] [nvarchar](50) NULL DEFAULT ('NS'),
	[ProfitLossBdgtOpt] [nvarchar](50) NULL DEFAULT ('NS'),
	[RecCrryInLowerLevel] [nvarchar](50) NULL DEFAULT ('NS'),
	[RecCrryInLowerLevelCtrl] [nvarchar](50) NULL DEFAULT ('NS'),
	[RecCrryInAMCtrl] [nvarchar](50) NULL DEFAULT ('NS'),
	[BdgtCtrl] [nvarchar](50) NULL DEFAULT ('NS'),
	[PstdCtrl] [nvarchar](50) NULL DEFAULT ('NS'),
	[PreCommSpngCtrl] [nvarchar](50) NULL DEFAULT ('NS'),
	[CommSpngCtrl] [nvarchar](50) NULL DEFAULT ('NS'),
	[ObligSpngCtrl] [nvarchar](50) NULL DEFAULT ('NS'),
	[AccrSpngCtrl] [nvarchar](50) NULL DEFAULT ('NS'),
	[ExpndSpngCtrl] [nvarchar](50) NULL DEFAULT ('NS'),
	[ExpnsSpngCtrl] [nvarchar](50) NULL DEFAULT ('NS'),
	[ReimSpngCtrl] [nvarchar](50) NULL DEFAULT ('NS'),
	[ReimAgreSpngCtrl] [nvarchar](50) NULL DEFAULT ('NS'),
	[FteBdgtCtrl] [nvarchar](50) NULL DEFAULT ('NS'),
	[FteSpngCtrl] [nvarchar](50) NULL DEFAULT ('NS'),
	[TransactionTypeCtrl] [nvarchar](50) NULL DEFAULT ('NS'),
	[AuthorityDistributionCtrl] [nvarchar](50) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BudgetDocuments]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BudgetDocuments](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[EFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetLevel] [nvarchar](80) NULL DEFAULT ('NS'),
	[DocumentDate] [datetime] NULL,
	[LastDocumentDate] [datetime] NULL,
	[DocumentType] [nvarchar](80) NULL DEFAULT ('NS'),
	[DocumentNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundName] [nvarchar](80) NULL DEFAULT ('NS'),
	[RpioCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RpioName] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhName] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgName] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaName] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ReimbursableAgreementControls] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetingControls] [nvarchar](80) NULL DEFAULT ('NS'),
	[PostingControls] [nvarchar](80) NULL DEFAULT ('NS'),
	[PreCommitmentControls] [nvarchar](80) NULL DEFAULT ('NS'),
	[CommitmentControls] [nvarchar](80) NULL DEFAULT ('NS'),
	[ObligationControls] [nvarchar](80) NULL DEFAULT ('NS'),
	[ExpenditureControls] [nvarchar](80) NULL DEFAULT ('NS'),
	[ExpenseControls] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccrualControls] [nvarchar](80) NULL DEFAULT ('NS'),
	[ReimbursementControls] [nvarchar](80) NULL DEFAULT ('NS'),
	[Budgeted] [float] NULL DEFAULT (0.0),
	[Posted] [float] NULL DEFAULT (0.0),
	[CarryOut] [float] NULL DEFAULT (0.0),
	[CarryIn] [float] NULL DEFAULT (0.0),
	[EstimatedRecoveries] [float] NULL DEFAULT (0.0),
	[EstimatedReimbursements] [float] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CarryoverEstimates]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CarryoverEstimates](
	[CarryoverEstimateId] [int] IDENTITY(1,1) NOT NULL,
	[BudgetLevel] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundName] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[DivisionName] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[Balance] [real] NULL,
	[OpenCommitment] [real] NULL,
	[Estimate] [real] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Changes]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Changes](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[TableName] [nvarchar](80) NULL DEFAULT ('NS'),
	[FieldName] [nvarchar](80) NULL DEFAULT ('NS'),
	[Action] [nvarchar](80) NULL DEFAULT ('NS'),
	[OldValue] [nvarchar](80) NULL DEFAULT ('NS'),
	[NewValue] [nvarchar](80) NULL DEFAULT ('NS'),
	[TimeStamp] [datetime] NULL,
	[Message] [nvarchar](255) NULL DEFAULT ('NOT SPECIFIED')
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CPIC]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CapitalPlanningInvestmentCodes](
	[CapitalPlanningInvestmentCodesId] [int] IDENTITY(1,1) NOT NULL,
	[Code] [nvarchar](255) NOT NULL,
	[CostAreaCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[CostAreaName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProjectName] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Defactos]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Defactos](
	[DefactoId] [int] IDENTITY(1,1) NOT NULL,
	[StatusOfFundsId] [int] NULL,
	[BudgetLevel] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[EFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[RpioCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RpioName] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhName] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundName] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgName] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](50) NULL,
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaName] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcName] [nvarchar](80) NULL DEFAULT ('NS'),
	[LowerName] [nvarchar](80) NULL DEFAULT ('NS'),
	[Amount] [float] NULL DEFAULT (0.0),
	[Budgeted] [float] NULL DEFAULT (0.0),
	[Posted] [float] NULL DEFAULT (0.0),
	[OpenCommitments] [float] NULL DEFAULT (0.0),
	[ULO] [float] NULL DEFAULT (0.0),
	[Expenditures] [float] NULL DEFAULT (0.0),
	[Obligations] [float] NULL DEFAULT (0.0),
	[Used] [float] NULL DEFAULT (0.0),
	[Available] [float] NULL DEFAULT (0.0),
	[NpmCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmName] [nvarchar](100) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Deobligations]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Deobligations](
	[DeobligationId] [int] IDENTITY(1,1) NOT NULL,
	[RPIO] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[DocumentNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[CalendarYear] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[Date] [datetime] NULL,
	[Amount] [float] NULL DEFAULT (0.0)
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ExecutionTables]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ExecutionTables](
	[ExecutionTableId] [int] IDENTITY(1,1) NOT NULL,
	[TableName] [nvarchar](80) NULL DEFAULT ('NS'),
	[Type] [nvarchar](50) NULL DEFAULT ('NS')
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[FullTimeEquivalents]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[FullTimeEquivalents](
	[FullTimeEquivalentId] [int] IDENTITY(1,1) NOT NULL,
	[PrcId] [int] NOT NULL,
	[BudgetLevel] [nvarchar](80) NULL DEFAULT ('NS'),
	[RPIO] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[Amount] [float] NULL DEFAULT (0.0),
	[FundName] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[Division] [nvarchar](80) NULL DEFAULT ('NS'),
	[DivisionName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ActivityCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaName] [nvarchar](80) NULL DEFAULT ('NS'),
	[GoalCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[GoalName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ObjectiveCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ObjectiveName] [nvarchar](80) NULL DEFAULT ('NS'),
	[AllocationRatio] [float] NULL DEFAULT (0.0),
	[ChangeDate] [datetime] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Obligations]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Obligations](
	[ObligationId] [int] IDENTITY(1,1) NOT NULL,
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[EFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[RpioCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RpioName] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhName] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundName] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgName] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectName] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcName] [nvarchar](80) NULL DEFAULT ('NS'),
	[DocumentType] [nvarchar](80) NULL DEFAULT ('NS'),
	[DocumentNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[DocumentControlNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[ReferenceDocumentNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProcessedDate] [datetime] NULL,
	[LastActivityDate] [datetime] NULL,
	[Age] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[FocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[FocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmName] [nvarchar](80) NULL DEFAULT ('NS'),
	[VendorCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[VendorName] [nvarchar](80) NULL DEFAULT ('NS'),
	[OpenCommitments] [float] NULL DEFAULT (0.0),
	[Obligations] [float] NULL DEFAULT (0.0),
	[ULO] [float] NULL DEFAULT (0.0),
	[Expenditures] [float] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[OperatingPlans]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[OperatingPlans](
	[OperatingPlanId] [int] IDENTITY(1,1) NOT NULL,
	[RpioCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RpioName] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[EFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[Amount] [float] NULL DEFAULT (0.0),
	[ITProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProjectName] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProjectTypeName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProjectTypeCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmName] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhName] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundName] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgName] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ActivityCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ActivityName] [nvarchar](80) NULL DEFAULT ('NS'),
	[LocalCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[LocalCodeName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaName] [nvarchar](80) NULL DEFAULT ('NS'),
	[CostAreaCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[CostAreaName] [nvarchar](80) NULL DEFAULT ('NS'),
	[GoalCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[GoalName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ObjectiveCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ObjectiveName] [text] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PayPeriods]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PayPeriods](
	[PayPeriodId] [int] IDENTITY(1,1) NOT NULL,
	[Period] [nvarchar](255) NOT NULL,
	[PayPeriod] [nvarchar](80) NULL DEFAULT ('NS'),
	[StartDate] [datetime] NULL,
	[EndDate] [datetime] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PayrollActivity]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PayrollActivity](
	[PayrollActivityId] [int] IDENTITY(1,1) NOT NULL,
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[EFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[RpioCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RpioName] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundName] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhName] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcName] [nvarchar](80) NULL DEFAULT ('NS'),
	[SubRcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[SubRcName] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaName] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmName] [text] NOT NULL,
	[FocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[FocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[HrOrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[HrOrgName] [nvarchar](80) NULL DEFAULT ('NS'),
	[WorkCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[WorkCodeName] [nvarchar](80) NULL DEFAULT ('NS'),
	[PayPeriod] [nvarchar](80) NULL DEFAULT ('NS'),
	[StartDate] [datetime] NULL,
	[EndDate] [datetime] NULL,
	[CheckDate] [datetime] NULL,
	[Amount] [float] NULL DEFAULT (0.0),
	[Hours] [float] NULL DEFAULT (0.0),
	[BasePaid] [float] NULL DEFAULT (0.0),
	[BaseHours] [float] NULL DEFAULT (0.0),
	[Benefits] [float] NULL DEFAULT (0.0),
	[OvertimePaid] [float] NULL DEFAULT (0.0),
	[OvertimeHours] [float] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PayrollAuthority]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PayrollAuthority](
	[PayrollId] [int] IDENTITY(1,1) NOT NULL,
	[AllocationsId] [int] NOT NULL,
	[StatusOfFundsId] [int] NOT NULL,
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[EFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[RpioCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RpioName] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetLevel] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhName] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundName] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgName] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcName] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocCode] [tinyint] NULL,
	[BocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[Amount] [float] NULL DEFAULT (0.0),
	[ProgramProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaName] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmName] [text] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PayrollCostCodes]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PayrollCostCodes](
	[PayrollCostCodeId] [int] IDENTITY(1,1) NOT NULL,
	[RPIO] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[DivisionName] [nvarchar](80) NULL DEFAULT ('NS'),
	[WorkCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[WorkCodeName] [nvarchar](80) NULL DEFAULT ('NS'),
	[HrOrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[HrOrgName] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ProgramFinancingSchedule]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ProgramFinancingSchedule](
	[ID] [int] NOT NULL,
	[ReportFiscalYear] [nvarchar](80) NULL DEFAULT ('NS'),
	[ReportFiscalMonth] [nvarchar](80) NULL DEFAULT ('NS'),
	[ReportFiscalQuarter] [nvarchar](80) NULL DEFAULT ('NS'),
	[FY1] [nvarchar](80) NULL DEFAULT ('NS'),
	[FY2] [nvarchar](80) NULL DEFAULT ('NS'),
	[TRACCT] [nvarchar](80) NULL DEFAULT ('NS'),
	[SGL_ACCT] [nvarchar](80) NULL DEFAULT ('NS'),
	[LINENO] [nvarchar](80) NULL DEFAULT ('NS'),
	[AMT] [float] NULL DEFAULT (0.0),
	[AMT_ORIG] [float] NULL DEFAULT (0.0),
	[BUD_AMT] [float] NULL DEFAULT (0.0),
	[AGY_AMT] [float] NULL DEFAULT (0.0),
	[SECTION_NO] [nvarchar](80) NULL DEFAULT ('NS'),
	[SECTION_NAME] [nvarchar](80) NULL DEFAULT ('NS'),
	[LINE_DESC_SHORT] [nvarchar](80) NULL DEFAULT ('NS'),
	[BUDGET_ACCT_ID] [nvarchar](80) NULL DEFAULT ('NS'),
	[ACCT] [nvarchar](80) NULL DEFAULT ('NS'),
	[AGESEQ] [nvarchar](80) NULL DEFAULT ('NS'),
	[ACCTSEQ] [nvarchar](80) NULL DEFAULT ('NS'),
	[AGETL] [nvarchar](80) NULL DEFAULT ('NS'),
	[BURTL] [nvarchar](80) NULL DEFAULT ('NS'),
	[ACCTTL] [nvarchar](80) NULL DEFAULT ('NS'),
	[TRACCTTL] [nvarchar](80) NULL DEFAULT ('NS'),
	[TRAG_ALLO_TRAC] [nvarchar](80) NULL DEFAULT ('NS'),
	[Year2Year1] [nvarchar](80) NULL DEFAULT ('NS'),
	[FLTR_AGETL] [nvarchar](80) NULL DEFAULT ('NS'),
	[FLTR_BUDGET_ACCT_ID] [nvarchar](80) NULL DEFAULT ('NS'),
 CONSTRAINT [PK_ProgramFinancingSchedule] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[RegionalAuthority]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[RegionalAuthority](
	[RescissionId] [int] IDENTITY(1,1) NOT NULL,
	[PrcId] [int] NULL,
	[RPIO] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetLevel] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ActivityCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[Allocation] [float] NULL DEFAULT (0.0),
	[Reduction] [float] NULL DEFAULT (0.0),
	[Amount] [float] NULL DEFAULT (0.0),
	[FundName] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[Division] [nvarchar](80) NULL DEFAULT ('NS'),
	[DivisionName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectName] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmName] [nvarchar](80) NULL DEFAULT ('NS'),
	[GoalCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[GoalName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ObjectiveCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ObjectiveName] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ReimbursableAgreements]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ReimbursableAgreements](
	[ReimbursableAgreementId] [int] IDENTITY(1,1) NOT NULL,
	[RPIO] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AgreementNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[StartDate] [datetime] NULL,
	[EndDate] [datetime] NULL,
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[DivisionName] [nvarchar](80) NULL DEFAULT ('NS'),
	[SiteProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[VendorCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[VendorName] [nvarchar](80) NULL DEFAULT ('NS'),
	[Amount] [float] NULL DEFAULT (0.0),
	[OpenCommitments] [float] NULL DEFAULT (0.0),
	[Obligations] [float] NULL DEFAULT (0.0),
	[ULO] [float] NULL DEFAULT (0.0),
	[Available] [money] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ReimbursableFunds]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ReimbursableFunds](
	[ReimbursableFundId] [int] IDENTITY(1,1) NOT NULL,
	[RPIO] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[DivisionName] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[DocumentControlNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[AgreeementNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[Amount] [float] NULL DEFAULT (0.0),
	[OpenCommitments] [float] NULL DEFAULT (0.0),
	[Obligations] [float] NULL DEFAULT (0.0),
	[ULO] [float] NULL DEFAULT (0.0),
	[Available] [money] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Reprogrammings]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Reprogrammings](
	[ReprogrammingId] [int] IDENTITY(1,1) NOT NULL,
	[ReprogrammingNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProcessedDate] [nvarchar](80) NULL DEFAULT ('NS'),
	[RPIO] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundName] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaName] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[DivisionName] [nvarchar](80) NULL DEFAULT ('NS'),
	[Amount] [numeric](18, 0) NULL,
	[SPIO] [nvarchar](80) NULL DEFAULT ('NS'),
	[Purpose] [nvarchar](80) NULL DEFAULT ('NS'),
	[ExtendedPurpose] [nvarchar](80) NULL DEFAULT ('NS'),
	[FromTo] [nvarchar](80) NULL DEFAULT ('NS'),
	[DocType] [nvarchar](80) NULL DEFAULT ('NS'),
	[DocPrefix] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[Line] [nvarchar](80) NULL DEFAULT ('NS'),
	[Subline] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SF132]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SF132](
	[ID] [int] IDENTITY(713,1) NOT NULL,
	[FiscalYear] [nvarchar](80) NULL DEFAULT ('NS'),
	[ActivityID] [nvarchar](80) NULL DEFAULT ('NS'),
	[TAFS] [nvarchar](80) NULL DEFAULT ('NS'),
	[FilteronTAFS] [nvarchar](80) NULL DEFAULT ('NS'),
	[TAFS10] [nvarchar](80) NULL DEFAULT ('NS'),
	[FilteronTAFS10] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAgency] [nvarchar](80) NULL DEFAULT ('NS'),
	[AllocationAgency] [nvarchar](80) NULL DEFAULT ('NS'),
	[AllocationSubaccount] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAccount] [nvarchar](80) NULL DEFAULT ('NS'),
	[BeginPeriodOfAvailability] [nvarchar](80) NULL DEFAULT ('NS'),
	[EndPeriodOfAvailability] [nvarchar](80) NULL DEFAULT ('NS'),
	[AvailabilityType] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAccountTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[AllocationAgencyTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetAgency] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetBureau] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetAccount] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetAgencyTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetBureauTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetAccountTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAgencyTAFS10] [nvarchar](80) NULL DEFAULT ('NS'),
	[AllocationAccount10] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAccount10] [nvarchar](80) NULL DEFAULT ('NS'),
	[FY1TAFS10] [nvarchar](80) NULL DEFAULT ('NS'),
	[FY2TAFS10] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetAgencySeq] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetBureauSeq] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetAccountSeq] [nvarchar](80) NULL DEFAULT ('NS'),
	[ApprovalDate] [nvarchar](80) NULL DEFAULT ('NS'),
	[ApprovedFootnoteId] [nvarchar](80) NULL DEFAULT ('NS'),
	[ApportionmentLineNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[LineSplit] [nvarchar](80) NULL DEFAULT ('NS'),
	[LineStub] [nvarchar](80) NULL DEFAULT ('NS'),
	[ApprovedAmount] [float] NULL DEFAULT (0.0),
	[LineSort] [nvarchar](80) NULL DEFAULT ('NS'),
	[FootnoteNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[FootnoteText] [text] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SF133]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SF133](
	[ID] [int] IDENTITY(713,1) NOT NULL,
	[ReportYear] [nvarchar](80) NULL DEFAULT ('NS'),
	[AGENCY] [nvarchar](80) NULL DEFAULT ('NS'),
	[BUREAU] [nvarchar](80) NULL DEFAULT ('NS'),
	[OmbAccount] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAccountGroup] [nvarchar](80) NULL DEFAULT ('NS'),
	[AllocationAccount] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAccount] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[EFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[STAT] [nvarchar](80) NULL DEFAULT ('NS'),
	[CreditIndicator] [nvarchar](80) NULL DEFAULT ('NS'),
	[COHORT] [nvarchar](80) NULL DEFAULT ('NS'),
	[LineNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[LineDescription] [nvarchar](80) NULL DEFAULT ('NS'),
	[Category] [nvarchar](80) NULL DEFAULT ('NS'),
	[TAFS] [nvarchar](80) NULL DEFAULT ('NS'),
	[AgencyTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[LastUpdated] [datetime] NULL,
	[SECTION] [nvarchar](80) NULL DEFAULT ('NS'),
	[SectionNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[LineType] [nvarchar](80) NULL DEFAULT ('NS'),
	[TafsAccount] [nvarchar](80) NULL DEFAULT ('NS'),
	[BureauTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[OmbAccountTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[FinancingAccounts] [nvarchar](80) NULL DEFAULT ('NS'),
	[AMT_NOV] [float] NULL DEFAULT (0.0),
	[AMT_JAN] [float] NULL DEFAULT (0.0),
	[AMT_FEB] [float] NULL DEFAULT (0.0),
	[AMT_APR] [float] NULL DEFAULT (0.0),
	[AMT_MAY] [float] NULL DEFAULT (0.0),
	[AMT_JUL] [float] NULL DEFAULT (0.0),
	[AMT_AUG] [float] NULL DEFAULT (0.0),
	[AGEUP] [nvarchar](80) NULL DEFAULT ('NS'),
	[AMT_OCT] [float] NULL DEFAULT (0.0),
	[AMT1] [float] NULL DEFAULT (0.0),
	[AMT2] [float] NULL DEFAULT (0.0),
	[AMT3] [float] NULL DEFAULT (0.0),
	[AMT4] [float] NULL DEFAULT (0.0),
	[LineShortDescription] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramCategory] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramCategoryStub] [nvarchar](80) NULL DEFAULT ('NS'),
	[CategoryStub] [text] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SiteProjectCodes]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SiteProjectCodes](
	[SiteProjectCodeId] [int] IDENTITY(713,1) NOT NULL,
	[RpioCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RpioName] [nvarchar](80) NULL DEFAULT ('NS'),
	[State] [nvarchar](80) NULL DEFAULT ('NS'),
	[CongressionalDistrict] [nvarchar](80) NULL DEFAULT ('NS'),
	[EpaSiteId] [nvarchar](80) NULL DEFAULT ('NS'),
	[SiteProjectName] [nvarchar](80) NULL DEFAULT ('NS'),
	[SiteProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[SSID] [nvarchar](80) NULL DEFAULT ('NS'),
	[ActionCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OperableUnit] [nvarchar](80) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[StateGrantObligations]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[StateGrantObligations](
	[StateGrantObligationId] [int] IDENTITY(1,1) NOT NULL,
	[RpioCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RpioName] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundName] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhName] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgName] [nvarchar](80) NULL DEFAULT ('NS'),
	[StateCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[StateName] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectName] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcName] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[Amount] [float] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[StatusOfFunds]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[StatusOfFunds](
	[StatusOfFundsId] [int] IDENTITY(1,1) NOT NULL,
	[BudgetLevel] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectName] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[LowerName] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcName] [nvarchar](80) NULL DEFAULT ('NS'),
	[DivisionName] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgName] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundName] [nvarchar](80) NULL DEFAULT ('NS'),
	[Amount] [float] NULL DEFAULT (0.0),
	[OpenCommitments] [float] NULL DEFAULT (0.0),
	[ULO] [float] NULL DEFAULT (0.0),
	[Total Expense Accruals] [float] NULL DEFAULT (0.0),
	[Expenditures] [float] NULL DEFAULT (0.0),
	[Obligations] [float] NULL DEFAULT (0.0),
	[Used] [float] NULL DEFAULT (0.0),
	[Available] [float] NULL DEFAULT (0.0),
	[NpmCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmName] [nvarchar](80) NULL DEFAULT ('NS'),
	[NpmTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaCode] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SuperfundSites]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SuperfundSites](
	[SiteId] [int] NOT NULL,
	[RpioCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RpioName] [nvarchar](80) NULL DEFAULT ('NS'),
	[City] [nvarchar](80) NULL DEFAULT ('NS'),
	[State] [nvarchar](80) NULL DEFAULT ('NS'),
	[SSID] [nvarchar](80) NULL DEFAULT ('NS'),
	[SiteProjectName] [nvarchar](80) NULL DEFAULT ('NS'),
	[EpaSiteId] [nvarchar](80) NULL DEFAULT ('NS'),
 CONSTRAINT [PK_SuperfundSites] PRIMARY KEY CLUSTERED 
(
	[SiteId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TAFS]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TAFS](
	[TafsId] [int] IDENTITY(713,1) NOT NULL,
	[FiscalYear] [nvarchar](80) NULL DEFAULT ('NS'),
	[ActivityID] [nvarchar](80) NULL DEFAULT ('NS'),
	[TAFS] [nvarchar](80) NULL DEFAULT ('NS'),
	[FilteronTAFS] [nvarchar](80) NULL DEFAULT ('NS'),
	[TAFS_10] [nvarchar](80) NULL DEFAULT ('NS'),
	[FilteronTAFS_10] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAgency] [nvarchar](80) NULL DEFAULT ('NS'),
	[AllocationAgency] [nvarchar](80) NULL DEFAULT ('NS'),
	[AllocationSubaccount] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAccountNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[EFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[AvailabilityType] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAccountTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[AllocationAgencyTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetAgency] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetBureau] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetAccount] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetAgencyTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetBureauTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetAccountTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAgencyTAF] [nvarchar](80) NULL DEFAULT ('NS'),
	[AllocationAccount] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAccount] [nvarchar](80) NULL DEFAULT ('NS'),
	[FY1TAFS] [nvarchar](80) NULL DEFAULT ('NS'),
	[FY2TAFS] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetAgencySeq] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetBureauSeq] [nvarchar](80) NULL DEFAULT ('NS'),
	[BudgetAccountSeq] [nvarchar](80) NULL DEFAULT ('NS'),
	[ApprovedDate] [datetime] NULL,
	[RequestDate] [datetime] NULL,
	[LastDate] [nvarchar](80) NULL DEFAULT ('NS'),
	[Transfers] [nvarchar](80) NULL DEFAULT ('NS'),
	[Warrants] [nvarchar](80) NULL DEFAULT ('NS'),
	[Exempt] [text] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Transfers]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Transfers](
	[TransferId] [int] IDENTITY(713,1) NOT NULL,
	[BudgetLevel] [nvarchar](80) NULL DEFAULT ('NS'),
	[DocType] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[RPIO] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundName] [nvarchar](80) NULL DEFAULT ('NS'),
	[DocumentNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProcessedDate] [datetime] NULL,
	[AhCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhName] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgName] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[DivisionName] [nvarchar](80) NULL DEFAULT ('NS'),
	[Code] [nvarchar](255) NOT NULL,
	[ProgramAreaCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramAreaName] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ResourceType] [nvarchar](80) NULL DEFAULT ('NS'),
	[Line] [float] NULL DEFAULT (0.0),
	[Subline] [float] NULL DEFAULT (0.0),
	[FromTo] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[Amount] [float] NULL DEFAULT (0.0),
	[Purpose] [nvarchar](80) NULL DEFAULT ('NS')
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TravelActivity]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TravelActivity](
	[TravelActivityId] [int] IDENTITY(1,1) NOT NULL,
	[RpioCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RpioName] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[AhName] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[FundName] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[ProgramProjectName] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OrgName] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[BocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[RcName] [nvarchar](80) NULL DEFAULT ('NS'),
	[FocCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[FocName] [nvarchar](80) NULL DEFAULT ('NS'),
	[FirstName] [nvarchar](80) NULL DEFAULT ('NS'),
	[LastName] [nvarchar](80) NULL DEFAULT ('NS'),
	[StartDate] [datetime] NULL,
	[EndDate] [datetime] NULL,
	[Duration] [float] NULL DEFAULT (0.0),
	[DocumentControlNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[Obligations] [float] NULL DEFAULT (0.0),
	[ULO] [float] NULL DEFAULT (0.0),
	[Expenditures] [float] NULL DEFAULT (0.0),
	[Extra] [float] NULL DEFAULT (0.0)
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TreasuryAppropriationFundSymbols]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TreasuryAppropriationFundSymbols](
	[ID] [int] NOT NULL,
	[FiscalYear] [nvarchar](80) NULL DEFAULT ('NS'),
	[ActivityID] [nvarchar](80) NULL DEFAULT ('NS'),
	[TafsCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[TafsCaption] [nvarchar](80) NULL DEFAULT ('NS'),
	[TAFS_10] [nvarchar](80) NULL DEFAULT ('NS'),
	[TafsCaption_10] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAgency] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAgencyCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAccount] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAccountTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[EFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[OmbAgencyCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OmbAgencyTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[OmbBureauCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OmbBureauTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[OmbAccountCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[OmbAccountTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[BeginningPeriodOfAvailability] [nvarchar](80) NULL DEFAULT ('NS'),
	[EndingPeriodOfAvailability] [nvarchar](80) NULL DEFAULT ('NS'),
	[AgencySequence] [nvarchar](80) NULL DEFAULT ('NS'),
	[BureauSequence] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountSequence] [nvarchar](80) NULL DEFAULT ('NS'),
	[LatestApprovedApportionmentDate] [nvarchar](80) NULL DEFAULT ('NS'),
	[LatestApportionmentRequestDate] [nvarchar](80) NULL DEFAULT ('NS'),
	[LatestSF133Date] [nvarchar](80) NULL DEFAULT ('NS'),
 CONSTRAINT [PK_TreasuryAppropriationFundSymbols] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TreasuryStatements]    Script Date: 12/12/2021 2:33:41 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TreasuryStatements](
	[ID] [int] NOT NULL,
	[FiscalYear] [nvarchar](80) NULL DEFAULT ('NS'),
	[LineNumber] [nvarchar](80) NULL DEFAULT ('NS'),
	[LineTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[TaxationCode] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAgency] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAccount] [nvarchar](80) NULL DEFAULT ('NS'),
	[SubAccount] [nvarchar](80) NULL DEFAULT ('NS'),
	[BFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[EFY] [nvarchar](80) NULL DEFAULT ('NS'),
	[OmbAgency] [nvarchar](80) NULL DEFAULT ('NS'),
	[OmbBureau] [nvarchar](80) NULL DEFAULT ('NS'),
	[OmbAccount] [nvarchar](80) NULL DEFAULT ('NS'),
	[AgencySequence] [nvarchar](80) NULL DEFAULT ('NS'),
	[BureauSequence] [nvarchar](80) NULL DEFAULT ('NS'),
	[AccountSequence] [nvarchar](80) NULL DEFAULT ('NS'),
	[AgencyTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[BureauTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[OmbAccountTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[TreasuryAccountTitle] [nvarchar](80) NULL DEFAULT ('NS'),
	[October] [float] NULL DEFAULT (0.0),
	[November] [float] NULL DEFAULT (0.0),
	[December] [float] NULL DEFAULT (0.0),
	[January] [float] NULL DEFAULT (0.0),
	[Feburary] [float] NULL DEFAULT (0.0),
	[March] [float] NULL DEFAULT (0.0),
	[April] [float] NULL DEFAULT (0.0),
	[May] [float] NULL DEFAULT (0.0),
	[June] [float] NULL DEFAULT (0.0),
	[July] [float] NULL DEFAULT (0.0),
	[August] [float] NULL DEFAULT (0.0),
	[September] [float] NULL
) ON [PRIMARY]
GO


