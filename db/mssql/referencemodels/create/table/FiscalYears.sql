CREATE TABLE [dbo].[FiscalYears]
(
	[FiscalYearId] [int] IDENTITY(1,1) NOT NULL,
	[BFY] [nvarchar](255) NOT NULL,
	[EFY] [nvarchar](255) NULL,
	[FirstYear] [nvarchar](255) NULL,
	[LastYear] [nvarchar](255) NULL,
	[ExpiringYear] [nvarchar](255) NULL,
	[StartDate] [datetime] NULL,
	[EndDate] [datetime] NULL,
	[Availability] [nvarchar](255) NULL,
	[Columbus] [datetime] NULL,
	[Thanksgiving] [datetime] NULL,
	[Christmas] [datetime] NULL,
	[NewYears] [datetime] NULL,
	[MartinLutherKing] [datetime] NULL,
	[Presidents] [datetime] NULL,
	[Memorial] [datetime] NULL,
	[Veterans] [datetime] NULL,
	[Labor] [datetime] NULL,
	[WorkDays] [float] NULL,
	[WeekDays] [float] NULL,
	[WeekEnds] [float] NULL
);
