CREATE TABLE IF NOT EXISTS "GrowthRates" 
(
	"GrowthRatesId"	INTEGER NOT NULL UNIQUE,
	"RateId"	TEXT NULL DEFAULT 'NS',
	"DESCRIPTION"	TEXT NULL DEFAULT 'NS',
	"BudgetYearRate"	NUMERIC NULL DEFAULT 0,
	"OutYear1"	NUMERIC NULL DEFAULT 0,
	"OutYear2"	NUMERIC NULL DEFAULT 0,
	"OutYear3"	NUMERIC NULL DEFAULT 0,
	"OutYear4"	NUMERIC NULL DEFAULT 0,
	"OutYear5"	NUMERIC NULL DEFAULT 0,
	"OutYear6"	NUMERIC NULL DEFAULT 0,
	"OutYear7"	NUMERIC NULL DEFAULT 0,
	"OutYear8"	NUMERIC NULL DEFAULT 0,
	"OutYear9"	NUMERIC NULL DEFAULT 0,
	"Sort"	TEXT NULL DEFAULT 'NS',
	PRIMARY KEY("GrowthRatesId" AUTOINCREMENT)
);