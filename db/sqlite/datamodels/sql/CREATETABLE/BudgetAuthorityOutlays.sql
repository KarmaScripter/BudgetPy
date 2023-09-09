CREATE TABLE IF NOT EXISTS BudgetAuthorityAndOutlays 
(
	BudgetAuthorityAndOutlaysId	INTEGER NOT NULL UNIQUE,
	ReportYear	TEXT(80) NULL DEFAULT NS,
	Category	TEXT(80) NULL DEFAULT NS,
	BudgetAccountName	TEXT(80) NULL DEFAULT NS,
	LineNumber	TEXT(80) NULL DEFAULT NS,
	LineName	TEXT(80) NULL DEFAULT NS,
	AccountType	TEXT(80) NULL DEFAULT NS,
	AuthorityType	TEXT(80) NULL DEFAULT NS,
	PriorYear	DOUBLE NULL DEFAULT 0.0,
	CurrentYear	DOUBLE NULL DEFAULT 0.0,
	BudgetYear	DOUBLE NULL DEFAULT 0.0,
	OutYear1	DOUBLE NULL DEFAULT 0.0,
	OutYear2	DOUBLE NULL DEFAULT 0.0,
	OutYear3	DOUBLE NULL DEFAULT 0.0,
	OutYear4	DOUBLE NULL DEFAULT 0.0,
	OutYear5	DOUBLE NULL DEFAULT 0.0,
	OutYear6	DOUBLE NULL DEFAULT 0.0,
	OutYear7	DOUBLE NULL DEFAULT 0.0,
	OutYear8	DOUBLE NULL DEFAULT 0.0,
	OutYear9	DOUBLE NULL DEFAULT 0.0,
	PRIMARY KEY(BudgetAuthorityAndOutlaysId AUTOINCREMENT)
);