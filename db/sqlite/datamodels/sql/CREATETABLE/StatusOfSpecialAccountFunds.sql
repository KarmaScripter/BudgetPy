CREATE TABLE IF NOT EXISTS StatusOfSpecialAccountFunds 
(
	StatusOfSpecialAccountFundsId	INTEGER NOT NULL UNIQUE,
	FiscalYear	TEXT(80) NULL DEFAULT NS,
	BFY	TEXT(80) NULL DEFAULT NS,
	EFY	TEXT(80) NULL DEFAULT NS,
	FundCode	TEXT(80) NULL DEFAULT NS,
	FundName	TEXT(80) NULL DEFAULT NS,
	RpioCode	TEXT(80) NULL DEFAULT NS,
	RpioName	TEXT(80) NULL DEFAULT NS,
	ProgramCode	TEXT(80) NULL DEFAULT NS,
	SpecialAccountNumber	TEXT(80) NULL DEFAULT NS,
	SpecialAccountName	TEXT(80) NULL DEFAULT NS,
	SpecialAccountStatus	TEXT(80) NULL DEFAULT NS,
	NplStatusCode	TEXT(80) NULL DEFAULT NS,
	StatusDescription	TEXT(80) NULL DEFAULT NS,
	EpaSiteId	TEXT(80) NULL DEFAULT NS,
	CerclisSiteId	TEXT(80) NULL DEFAULT NS,
	SiteCode	TEXT(80) NULL DEFAULT NS,
	SiteName	TEXT(80) NULL DEFAULT NS,
	OperableUnit	TEXT(80) NULL DEFAULT NS,
	PipelineCode	TEXT(80) NULL DEFAULT NS,
	PipelineDescription	TEXT(80) NULL DEFAULT NS,
	TransactionDescription	TEXT(80) NULL DEFAULT NS,
	InterestDate	TEXT(80) NULL DEFAULT NS,
	TrustfundTransfers	DOUBLE NULL DEFAULT 0.0,
	OpenCommitments	DOUBLE NULL DEFAULT 0.0,
	Obligations	DOUBLE NULL DEFAULT 0.0,
	UnliquidatedObligations	DOUBLE NULL DEFAULT 0.0,
	Disbursements	DOUBLE NULL DEFAULT 0.0,
	UnpaidBalance	DOUBLE NULL DEFAULT 0.0,
	CumulativeReceipts	DOUBLE NULL DEFAULT 0.0,
	NetReceipts	DOUBLE NULL DEFAULT 0.0,
	Interest	DOUBLE NULL DEFAULT 0.0,
	CollectionsAndInterest	DOUBLE NULL DEFAULT 0.0,
	AvailableBalance	DOUBLE NULL DEFAULT 0.0,
	PRIMARY KEY(StatusOfSpecialAccountFundsId AUTOINCREMENT)
);