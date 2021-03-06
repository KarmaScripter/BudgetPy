CREATE TABLE IF NOT EXISTS "ReimbursableAgreements" 
(
	"ReimbursableAgreementsId"	INTEGER NOT NULL,
	"RPIO"	TEXT(80) NULL DEFAULT "NS",
	"BFY"	TEXT(80) NULL DEFAULT "NS",
	"FundCode"	TEXT(80) NULL DEFAULT "NS",
	"AgreementNumber"	TEXT(80) NULL DEFAULT "NS",
	"StartDate"	TEXT(80) NULL DEFAULT "NS",
	"EndDate"	TEXT(80) NULL DEFAULT "NS",
	"RcCode"	TEXT(80) NULL DEFAULT "NS",
	"OrgCode"	TEXT(80) NULL DEFAULT "NS",
	"RcName"	TEXT(80) NULL DEFAULT "NS",
	"SiteProjectCode"	TEXT(80) NULL DEFAULT "NS",
	"AccountCode"	TEXT(80) NULL DEFAULT "NS",
	"VendorCode"	TEXT(80) NULL DEFAULT "NS",
	"VendorName"	TEXT(80) NULL DEFAULT "NS",
	"Amount"	REAL DEFAULT 0.0,
	"OpenCommitments"	REAL DEFAULT 0.0,
	"Obligations"	REAL DEFAULT 0.0,
	"ULO"	REAL DEFAULT 0.0,
	"Available"	REAL DEFAULT 0.0
);