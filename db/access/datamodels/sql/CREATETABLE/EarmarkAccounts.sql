CREATE TABLE EarmarkAccounts 
(
	EarmarkAccountsId AUTOINCREMENT NOT NULL UNIQUE,
	BFY	TEXT(100) DEFAULT NS,
	EFY	TEXT(100) DEFAULT NS,
	FundCode	TEXT(100) DEFAULT NS,
	FundName	TEXT(100) DEFAULT NS,
	RpioCode	TEXT(100) DEFAULT NS,
	RpioName	TEXT(100) DEFAULT NS,
	AhCode	TEXT(100) DEFAULT NS,
	AhName	TEXT(100) DEFAULT NS,
	NpmCode	TEXT(100) DEFAULT NS,
	NpmName	TEXT(100) DEFAULT NS,
	AccountCode	TEXT(100) DEFAULT NS,
	BocCode	TEXT(100) DEFAULT NS,
	BocName	TEXT(100) DEFAULT NS,
	ProgramProjectCode	TEXT(100) DEFAULT NS,
	ProgramProjectName	TEXT(100) DEFAULT NS,
	ProgramAreaCode	TEXT(100) DEFAULT NS,
	ProgramAreaName	TEXT(100) DEFAULT NS,
	StateCode	TEXT(100) DEFAULT NS,
	StateName	TEXT(100) DEFAULT NS,
	Project	TEXT(100) DEFAULT NS,
	Amount	DOUBLE DEFAULT 0.0,
	TreasuryAccountCode	TEXT(100) DEFAULT NS,
	TreasuryAccountName	TEXT(100) DEFAULT NS,
	BudgetAccountCode	TEXT(100) DEFAULT NS,
	BudgetAccountName	TEXT(100) DEFAULT NS
	CONSTRAINT(EarmarkAccountsPrimaryKey) )
		PRIMARY KEY(EarmarkAccountsId)
);