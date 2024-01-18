CREATE TABLE IF NOT EXISTS StatusOfAppropriations
(
	StatusOfAppropriationsId	INTEGER NOT NULL UNIQUE,
	BFY	TEXT(150) DEFAULT NS,
	EFY	TEXT(150) DEFAULT NS,
	BudgetLevel	TEXT(150) DEFAULT NS,
	FundCode	TEXT(150) DEFAULT NS,
	FundName	TEXT(150) DEFAULT NS,
	Availability	TEXT(150) DEFAULT NS,
	TransType	TEXT(150) DEFAULT NS,
	TreasurySymbol	TEXT(150) DEFAULT NS,
	OriginalAmount	DOUBLE DEFAULT 0.0,
	Authority	DOUBLE DEFAULT 0.0,
	Budgeted	DOUBLE DEFAULT 0.0,
	Posted	DOUBLE DEFAULT 0.0,
	EstimatedReimbursements	DOUBLE DEFAULT 0.0,
	ActualReimbursements	DOUBLE DEFAULT 0.0,
	EstimatedRecoveries	DOUBLE DEFAULT 0.0,
	AccrualRecoveries	DOUBLE DEFAULT 0.0,
	CarryoverOut	DOUBLE DEFAULT 0.0,
	CarryoverIn	DOUBLE DEFAULT 0.0,
	TransferIn	DOUBLE DEFAULT 0.0,
	TransferOut	DOUBLE DEFAULT 0.0,
	OpenCommitments	DOUBLE DEFAULT 0.0,
	Obligations	DOUBLE DEFAULT 0.0,
	UnliquidatedObligations	DOUBLE DEFAULT 0.0,
	Used	DOUBLE DEFAULT 0.0,
	Expenditures	DOUBLE DEFAULT 0.0,
	Available	DOUBLE DEFAULT 0.0,
	TreasuryAccountCode	TEXT(150) DEFAULT NS,
	TreasuryAccountName	TEXT(150) DEFAULT NS,
	BudgetAccountCode	TEXT(150) DEFAULT NS,
	BudgetAccountName	TEXT(150) DEFAULT NS,
	PRIMARY KEY(StatusOfAppropriationsId AUTOINCREMENT)
);