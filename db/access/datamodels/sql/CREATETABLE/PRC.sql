CREATE TABLE PRC
(
	PrcId           AUTOINCREMENT NOT NULL UNIQUE,
	StatusOfFundsId INT           NULL,
	BFY             TEXT( 150 )   NULL DEFAULT NS,
	EFY             TEXT( 150 )   NULL DEFAULT NS,
	FundCode        TEXT( 150 )   NULL DEFAULT NS,
	RpioCode        TEXT( 150 )   NULL DEFAULT NS,
	AhCode          TEXT( 150 )   NULL DEFAULT NS,
	OrgCode         TEXT( 150 )   NULL DEFAULT NS,
	AccountCode     TEXT( 150 )   NULL DEFAULT NS,
	BocCode         TEXT( 150 )   NULL DEFAULT NS, CONSTRAINT
(
	PRCPrimaryKey
)
	PRIMARY KEY
(
	PrcId
)
	);
