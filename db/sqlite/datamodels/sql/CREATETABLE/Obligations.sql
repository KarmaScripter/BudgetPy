CREATE TABLE IF NOT EXISTS "Obligations" 
(
	"ObligationsId"	INTEGER NOT NULL UNIQUE,
	"BFY"	TEXT(80) DEFAULT 'NS',
	"EFY"	TEXT(80) DEFAULT 'NS',
	"TreasurySymbol"	TEXT(80) DEFAULT 'NS',
	"FundCode"	TEXT(80) DEFAULT 'NS',
	"FundName"	TEXT(80) DEFAULT 'NS',
	"RpioCode"	TEXT(80) DEFAULT 'NS',
	"RpioName"	TEXT(80) DEFAULT 'NS',
	"AhCode"	TEXT(80) DEFAULT 'NS',
	"AhName"	TEXT(80) DEFAULT 'NS',
	"OrgCode"	TEXT(80) DEFAULT 'NS',
	"OrgName"	TEXT(80) DEFAULT 'NS',
	"AccountCode"	TEXT(80) DEFAULT 'NS',
	"ProgramProjectCode"	TEXT(80) DEFAULT 'NS',
	"ProgramProjectName"	TEXT(80) DEFAULT 'NS',
	"RcCode"	TEXT(80) DEFAULT 'NS',
	"RcName"	TEXT(80) DEFAULT 'NS',
	"DocumentType"	TEXT(80) DEFAULT 'NS',
	"DocumentNumber"	TEXT(80) DEFAULT 'NS',
	"DocumentControlNumber"	TEXT(80) DEFAULT 'NS',
	"BudgetAccountCode"	TEXT(80) DEFAULT 'NS',
	"BudgetAccountName"	TEXT(80) DEFAULT 'NS',
	"ApportionmentAccountCode"	TEXT(80) DEFAULT 'NS',
	"ProcessedDate"	TEXT(80) DEFAULT 'NS',
	"LastActivityDate"	TEXT(80) DEFAULT 'NS',
	"Age"	TEXT(80) DEFAULT 'NS',
	"BocCode"	TEXT(80) DEFAULT 'NS',
	"BocName"	TEXT(80) DEFAULT 'NS',
	"FocCode"	TEXT(80) DEFAULT 'NS',
	"FocName"	TEXT(80) DEFAULT 'NS',
	"NpmCode"	TEXT(80) DEFAULT 'NS',
	"NpmName"	TEXT(80) DEFAULT 'NS',
	"VendorCode"	TEXT(80) DEFAULT 'NS',
	"VendorName"	TEXT(80) DEFAULT 'NS',
	"OpenCommitments"	DECIMAL DEFAULT 0.0,
	"Obligations"	DECIMAL DEFAULT 0.0,
	"ULO"	DECIMAL DEFAULT 0.0,
	"Expenditures"	DECIMAL DEFAULT 0.0,
	PRIMARY KEY("ObligationsId" AUTOINCREMENT)
);