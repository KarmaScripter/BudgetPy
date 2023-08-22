CREATE TABLE IF NOT EXISTS ApportionmentData
(
	ApportionmentDataId INTEGER NOT NULL UNIQUE,
	FiscalYear	TEXT(80),
	BFY	TEXT(80) NULL DEFAULT NS,
	EFY	TEXT(80) NULL DEFAULT NS,
	TreasuryAccountCode	TEXT(80) NULL DEFAULT NS,
	TreasuryAccountName	TEXT(150) NULL DEFAULT NS,
	ApportionmentAccountCode	TEXT(80) NULL DEFAULT NS,
	ApportionmentAccountName	TEXT(150) NULL DEFAULT NS,
	AvailabilityType	TEXT(80) NULL DEFAULT NS,
	BudgetAccountCode	TEXT(80) NULL DEFAULT NS,
	BudgetAccountName	TEXT(150) NULL DEFAULT NS,
	ApprovalDate	TEXT(80) NULL DEFAULT NS,
	LineNumber	TEXT(80) NULL DEFAULT NS,
	LineName	TEXT(80) NULL DEFAULT NS,
	Amount	DOUBLE,
	FundCode	TEXT(80) NULL DEFAULT NS,
	FundName	TEXT(80) NULL DEFAULT NS,
    	PRIMARY KEY(ApportionmentDataId AUTOINCREMENT)
);