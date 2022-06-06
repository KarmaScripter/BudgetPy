CREATE TABLE IF NOT EXISTS "SpendingRates" 
(
	"SpendingRatesId"	INTEGER NOT NULL UNIQUE,
	"OmbAgencyCode"	TEXT(80) NULL DEFAULT 'NS',
	"OmbAgencyName"	TEXT(80) NULL DEFAULT 'NS',
	"OmbBureauCode"	TEXT(80) NULL DEFAULT 'NS',
	"OmbBureauName"	TEXT(80) NULL DEFAULT 'NS',
	"TreausuryAgencyCode"	TEXT(80) NULL DEFAULT 'NS',
	"TreausuryAccountCode"	TEXT(80) NULL DEFAULT 'NS',
	"TreausuryAccountName"	TEXT(80) NULL DEFAULT 'NS',
	"AccountTitle"	TEXT(80) NULL DEFAULT 'NS',
	"Subfunction"	TEXT(80) NULL DEFAULT 'NS',
	"Line"	TEXT(80) NULL DEFAULT 'NS',
	"LineNumber"	TEXT(80) NULL DEFAULT 'NS',
	"Category"	TEXT(80) NULL DEFAULT 'NS',
	"Subcategory"	TEXT(80) NULL DEFAULT 'NS',
	"SubcategoryName"	TEXT(80) NULL DEFAULT 'NS',
	"AccountCode"	TEXT(80) NULL DEFAULT 'NS',
	"Jurisdiction"	TEXT(80) NULL DEFAULT 'NS',
	"YearOfAuthority"	TEXT(80) NULL DEFAULT 'NS',
	"BudgetAuthority"	NUMERIC NULL DEFAULT 0.0,
	"OutYear1"	NUMERIC NULL DEFAULT 0.0,
	"OutYear2"	NUMERIC NULL DEFAULT 0.0,
	"OutYear3"	NUMERIC NULL DEFAULT 0.0,
	"OutYear4"	NUMERIC NULL DEFAULT 0.0,
	"OutYear5"	NUMERIC NULL DEFAULT 0.0,
	"OutYear6"	NUMERIC NULL DEFAULT 0.0,
	"OutYear7"	NUMERIC NULL DEFAULT 0.0,
	"OutYear8"	NUMERIC NULL DEFAULT 0.0,
	"OutYear9"	NUMERIC NULL DEFAULT 0.0,
	"OutYear10"	NUMERIC NULL DEFAULT 0.0,
	"OutYear11"	NUMERIC NULL DEFAULT 0.0,
	"TotalSpendout"	NUMERIC NULL DEFAULT 0.0,
	PRIMARY KEY("SpendingRatesId" AUTOINCREMENT)
);