CREATE TABLE IF NOT EXISTS CarryoverRequests
(
	CarryoverRequestsId INTEGER NOT NULL UNIQUE,
	Analyst TEXT(150) NULL DEFAULT NS,
	RpioCode TEXT(150) NULL DEFAULT NS,
	DocumentTitle TEXT(255) NULL DEFAULT NS,
	Amount DOUBLE NULL DEFAULT 0.0,
	FundCode TEXT(150) NULL DEFAULT NS,
	Status TEXT(150) NULL DEFAULT NS,
	OriginalRequestDate DATETIME NULL,
	LastActivityDate DATETIME NULL,
	BudgetFormulationSystem TEXT(150) NULL DEFAULT NS,
	Comments TEXT(MAX) NULL DEFAULT NS,
	RequestDocument TEXT(MAX) NULL DEFAULT NS,
	Duration DOUBLE NULL DEFAULT 0.0,
	CONSTRAINT CarryoverRequestsPrimaryKey 
		PRIMARY KEY(CarryoverRequestsId )
) ;
