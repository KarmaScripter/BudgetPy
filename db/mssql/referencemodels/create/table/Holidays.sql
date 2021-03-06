CREATE TABLE [dbo].[Holidays]
(
	[HolidayId] [int] IDENTITY(1,1) NOT NULL,
	[ColumbusDay] [datetime] NULL,
	[ThanksgivingDay] [datetime] NULL,
	[ChristmasDay] [datetime] NULL,
	[NewYearsDay] [datetime] NULL,
	[MartinLutherKingDay] [datetime] NULL,
	[PresidentsDay] [datetime] NULL,
	[MemorialDay] [datetime] NULL,
	[VeteransDay] [datetime] NULL,
	[LaborDay] [datetime] NULL,
 CONSTRAINT [PK_Holidays] PRIMARY KEY CLUSTERED 
(
	[HolidayId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
