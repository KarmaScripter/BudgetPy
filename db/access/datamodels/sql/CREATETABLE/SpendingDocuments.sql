CREATE TABLE SpendingDocuments 
(
	SpendingDocumentsId	AUTOINCREMENT NOT NULL UNIQUE,
	BFY	TEXT(80) NULL DEFAULT NS,
	EFY	TEXT(80) NULL DEFAULT NS,
	TreasurySymbol	TEXT(80) NULL DEFAULT NS,
	RpioCode	TEXT(80) NULL DEFAULT NS,
	RpioName	TEXT(80) NULL DEFAULT NS,
	FundCode	TEXT(80) NULL DEFAULT NS,
	FundName	TEXT(80) NULL DEFAULT NS,
	AhCode	TEXT(80) NULL DEFAULT NS,
	AhName	TEXT(80) NULL DEFAULT NS,
	AccountCode	TEXT(80) NULL DEFAULT NS,
	RpioActivityCode	TEXT(80) NULL DEFAULT NS,
	ProgramProjectName	TEXT(80) NULL DEFAULT NS,
	ProgramAreaCode	TEXT(80) NULL DEFAULT NS,
	ProgramAreaName	TEXT(80) NULL DEFAULT NS,
	PurchaseRequestNumber	TEXT(80) NULL DEFAULT NS,
	DocumentType	TEXT(80) NULL DEFAULT NS,
	DocumentControlNumber	TEXT(80) NULL DEFAULT NS,
	BocCode	TEXT(80) NULL DEFAULT NS,
	BocName	TEXT(80) NULL DEFAULT NS,
	OriginalActionDate	DATETIME NULL,
	LastActionDate	DATETIME NULL,
	Commitments	DOUBLE NULL DEFAULT 0.0,
	Obligations	DOUBLE NULL DEFAULT 0.0,
	Deobligations	DOUBLE NULL DEFAULT 0.0,
	UnliqudatedObligations	DOUBLE NULL DEFAULT 0.0,
	CONSTRAINT SpendingDocumentsPrimaryKey
        PRIMARY KEY(SpendingDocumentsId)
);