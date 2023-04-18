CREATE TABLE IF NOT EXISTS GeneralLedgerAccounts 
(
	GeneralLedgerAccountsId	INTEGER NOT NULL UNIQUE,
	BFY	TEXT(80) NULL DEFAULT 'NS',
	Number	TEXT(80) NULL DEFAULT 'NS',
	Name	TEXT(80) NULL DEFAULT 'NS',
	ShortName	TEXT(80) NULL DEFAULT 'NS',
	AccountClassification	TEXT(80) NULL DEFAULT 'NS',
	NormalBalance	TEXT(80) NULL DEFAULT 'NS',
	RealOrClosingAccount	TEXT(80) NULL DEFAULT 'NS',
	CashAccount	TEXT(80) NULL DEFAULT 'NS',
	SummaryAccount	TEXT(80) NULL DEFAULT 'NS',
	ReportableAccount	TEXT(80) NULL DEFAULT 'NS',
	CostAllocationIndicator	TEXT(80) NULL DEFAULT 'NS',
	FederalNonFederal	TEXT(80) NULL DEFAULT 'NS',
	AttributeValue	TEXT(80) NULL DEFAULT 'NS',
	Usage	TEXT(80) NULL DEFAULT 'NS',
	Deposit	TEXT(80) NULL DEFAULT 'NS',
	PRIMARY KEY(GeneralLedgerAccountsId AUTOINCREMENT)
);