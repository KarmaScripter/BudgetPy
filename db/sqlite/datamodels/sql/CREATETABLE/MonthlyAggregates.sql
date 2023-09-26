CREATE TABLE IF NOT EXISTS MonthlyAggregates 
(
	MarginalAggregatesId	INTEGER NOT NULL UNIQUE,
	BudgetAccountName	TEXT(80) NULL DEFAULT NS,
	MainAccount	TEXT(80) NULL DEFAULT NS,
	October	DOUBLE NULL DEFAULT 0.0,
	November	DOUBLE NULL DEFAULT 0.0,
	December	DOUBLE NULL DEFAULT 0.0,
	January	DOUBLE NULL DEFAULT 0.0,
	Feburary	DOUBLE NULL DEFAULT 0.0,
	March	DOUBLE NULL DEFAULT 0.0,
	April	DOUBLE NULL DEFAULT 0.0,
	May	DOUBLE NULL DEFAULT 0.0,
	June	DOUBLE NULL DEFAULT 0.0,
	July	DOUBLE NULL DEFAULT 0.0,
	August	DOUBLE NULL DEFAULT 0.0,
	September	DOUBLE NULL DEFAULT 0.0,
	PRIMARY KEY(MarginalAggregatesId AUTOINCREMENT)
);