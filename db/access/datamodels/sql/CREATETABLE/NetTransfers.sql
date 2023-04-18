CREATE TABLE NetTransfers 
(
 NetTransfersId AUTOINCREMENT NOT NULL UNIQUE,
 BFY TEXT(50) NULL DEFAULT NS,
 EFY TEXT(50) NULL DEFAULT NS,
 FundCode TEXT(50) NULL DEFAULT NS,
 FundName TEXT(50) NULL DEFAULT NS,
 RpioCode TEXT(50) NULL DEFAULT NS,
 RpioName TEXT(50) NULL DEFAULT NS,
 AhCode TEXT(50) NULL DEFAULT NS,
 AhName TEXT(50) NULL DEFAULT NS,
 OrgCode TEXT(50) NULL DEFAULT NS,
 OrgName TEXT(50) NULL DEFAULT NS,
 AccountCode TEXT(50) NULL DEFAULT NS,
 ProgramProjectName TEXT(50) NULL DEFAULT NS,
 BocCode TEXT(50) NULL DEFAULT NS,
 BocName TEXT(50) NULL DEFAULT NS,
 DocumentNumber TEXT(50) NULL DEFAULT NS,
 ProcessedDate TEXT(50) NULL DEFAULT NS,
 Net TEXT(50) NULL DEFAULT NS,
 Amount DOUBLE NULL DEFAULT 0.0,
 PRIMARY KEY( NetTransfersId )
);