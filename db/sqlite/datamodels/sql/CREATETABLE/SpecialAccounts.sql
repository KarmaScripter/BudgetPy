CREATE TABLE "SpecialAccounts" 
(
	"SpecialAccountsId"	INTEGER NOT NULL UNIQUE,
	"BFY"	TEXT(80) NULL DEFAULT 'NS',
	"RpioCode"	TEXT(80) NULL DEFAULT 'NS',
	"FundCode"	TEXT(80) NULL DEFAULT 'NS',
	"SpecialAccountFund"	TEXT(80) NULL DEFAULT 'NS',
	"SpecialAccountNumber"	TEXT(80) NULL DEFAULT 'NS',
	"SpecialAccountName"	TEXT(80) NULL DEFAULT 'NS',
	"AccountStatus"	TEXT(80) NULL DEFAULT 'NS',
	"NplStatusCode"	TEXT(80) NULL DEFAULT 'NS',
	"NplStatusName"	TEXT(80) NULL DEFAULT 'NS',
	"SiteId"	TEXT(80) NULL DEFAULT 'NS',
	"CerclisId"	TEXT(80) NULL DEFAULT 'NS',
	"SiteCode"	TEXT(80) NULL DEFAULT 'NS',
	"SiteName"	TEXT(80) NULL DEFAULT 'NS',
	"OperableUnit"	TEXT(80) NULL DEFAULT 'NS',
	"PipelineCode"	TEXT(80) NULL DEFAULT 'NS',
	"PipelineDescription"	TEXT(80) NULL DEFAULT 'NS',
	"AccountCode"	TEXT(80) NULL DEFAULT 'NS',
	"BocCode"	TEXT(80) NULL DEFAULT 'NS',
	"BocName"	TEXT(80) NULL DEFAULT 'NS',
	"TransactionType"	TEXT(80) NULL DEFAULT 'NS',
	"TransactionTypeName"	TEXT(80) NULL DEFAULT 'NS',
	"FocCode"	TEXT(80) NULL DEFAULT 'NS',
	"FocName"	TEXT(80) NULL DEFAULT 'NS',
	"TransactionDate"	TEXT(80) NULL DEFAULT 'NS',
	"AvailableBalance"	NUMERIC NULL DEFAULT 0,
	"OpenCommitments"	NUMERIC NULL DEFAULT 0,
	"Obligations"	NUMERIC NULL DEFAULT 0,
	"ULO"	NUMERIC NULL DEFAULT 0,
	"Disbursements"	NUMERIC NULL DEFAULT 0,
	"UnpaidBalances"	NUMERIC NULL DEFAULT 0,
	"Collections"	NUMERIC NULL DEFAULT 0,
	"CumulativeReceipts"	NUMERIC NULL DEFAULT 0,
	PRIMARY KEY("SpecialAccountsId" AUTOINCREMENT)
);