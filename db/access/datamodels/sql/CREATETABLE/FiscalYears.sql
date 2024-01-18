CREATE TABLE FiscalYears
(
	FiscalYearsId       AUTOINCREMENT  NOT NULL UNIQUE,
	BFY                 TEXT( 80 ) NOT NULL,
	EFY                 TEXT( 150 )    NULL DEFAULT NS,
	StartDate           TEXT( 150 )    NULL DEFAULT NS,
	ColumbusDay         DATETIME       NULL,
	VeteransDay         DATETIME       NULL,
	ThanksgivingDay     DATETIME       NULL,
	ChristmasDay        DATETIME       NULL,
	NewYearsDay         DATETIME       NULL,
	MartinLutherKingDay DATETIME       NULL,
	WashingtonsDay      DATETIME       NULL,
	MemorialDay         DATETIME       NULL,
	JuneteenthDay       DATETIME       NULL,
	IndependenceDay     DATETIME       NULL,
	LaborDay            DATETIME       NULL,
	ExpiringYear        TEXT( 150 )    NULL DEFAULT NS,
	ExpirationDate      TEXT( 150 )    NULL DEFAULT NS,
	WorkDays            DOUBLE         NULL DEFAULT 0.0,
	WeekDays            DOUBLE         NULL DEFAULT 0.0,
	WeekEnds            DOUBLE         NULL DEFAULT 0.0,
	EndDate             TEXT( 150 )    NULL DEFAULT NS,
	Availability        TEXT( 150 )    NULL DEFAULT NS, CONSTRAINT
(
	FiscalYearsPrimaryKey
)
	PRIMARY KEY
(
	FiscalYearsId
)
	);
