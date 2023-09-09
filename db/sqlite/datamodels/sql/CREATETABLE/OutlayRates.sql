CREATE TABLE IF NOT EXISTS OutlayRates 
(
	OutlayRatesId	INTEGER NOT NULL UNIQUE,
	FiscalYear TEXT(80) NULL DEFAULT NS,
	BudgetAccountCode TEXT(80) NULL DEFAULT NS,
	BudgetAccountName TEXT(80) NULL DEFAULT NS,
	Category TEXT(80) NULL DEFAULT NS,
	Baseline TEXT(80) NULL DEFAULT NS,
	Year1 DOUBLE NULL DEFAULT 0.0,
	Year2 DOUBLE NULL DEFAULT 0.0,
	Year3 DOUBLE NULL DEFAULT 0.0,
	Year4 DOUBLE NULL DEFAULT 0.0,
	Year5 DOUBLE NULL DEFAULT 0.0,
	Year6 DOUBLE NULL DEFAULT 0.0,
	Year7 DOUBLE NULL DEFAULT 0.0,
	Year8 DOUBLE NULL DEFAULT 0.0,
	Year9 DOUBLE NULL DEFAULT 0.0,
	Year10 DOUBLE NULL DEFAULT 0.0,
	Year11 DOUBLE NULL DEFAULT 0.0,
    PRIMARY KEY(OutlayRatesId AUTOINCREMENT)
);