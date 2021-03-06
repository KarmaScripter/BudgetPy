CREATE TABLE IF NOT EXISTS "GrossBudgetAuthorityOutlays" 
(
	"GrossBudgetAuthorityOutlaysId"	INTEGER NOT NULL UNIQUE,
	"ReportYear"	TEXT(80) NULL DEFAULT 'NS',
	"AgencyName"	TEXT(80) NULL DEFAULT 'NS',
	"OmbAccount"	TEXT(80) NULL DEFAULT 'NS',
	"Line"	TEXT(80) NULL DEFAULT 'NS',
	"LineNumber"	TEXT(80) NULL DEFAULT 'NS',
	"LineSection"	TEXT(80) NULL DEFAULT 'NS',
	"LineName"	TEXT(80) NULL DEFAULT 'NS',
	"BeaCategory"	TEXT(80) NULL DEFAULT 'NS',
	"BeaCategoryName"	TEXT(80) NULL DEFAULT 'NS',
	"LineCategory"	TEXT(80) NULL DEFAULT 'NS',
	"PriorYear"	NUMERIC NULL DEFAULT 0,
	"CurrentYear"	NUMERIC NULL DEFAULT 0,
	"BudgetYear"	NUMERIC NULL DEFAULT 0,
	"OutYear1"	NUMERIC NULL DEFAULT 0,
	"OutYear2"	NUMERIC NULL DEFAULT 0,
	"OutYear3"	NUMERIC NULL DEFAULT 0,
	"OutYear4"	NUMERIC NULL DEFAULT 0,
	"OutYear5"	NUMERIC NULL DEFAULT 0,
	"OutYear6"	NUMERIC NULL DEFAULT 0,
	"OutYear7"	NUMERIC NULL DEFAULT 0,
	"OutYear8"	NUMERIC NULL DEFAULT 0,
	"OutYear9"	NUMERIC NULL DEFAULT 0,
	PRIMARY KEY("GrossBudgetAuthorityOutlaysId" AUTOINCREMENT)
);