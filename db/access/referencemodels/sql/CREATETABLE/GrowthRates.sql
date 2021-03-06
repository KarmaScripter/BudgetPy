CREATE TABLE GrowthRates 
(
    GrowthRatesId INTEGER NOT NULL UNIQUE,
    RateId TEXT(80) NULL DEFAULT NS,
    DESCRIPTION TEXT(80) NULL DEFAULT NS,
    BudgetYearRate DOUBLE NULL DEFAULT 0.0,
    OutYear1 DOUBLE NULL DEFAULT 0.0,
    OutYear2 DOUBLE NULL DEFAULT 0.0,
    OutYear3 DOUBLE NULL DEFAULT 0.0,
    OutYear4 DOUBLE NULL DEFAULT 0.0,
    OutYear5 DOUBLE NULL DEFAULT 0.0,
    OutYear6 DOUBLE NULL DEFAULT 0.0,
    OutYear7 DOUBLE NULL DEFAULT 0.0,
    OutYear8 DOUBLE NULL DEFAULT 0.0,
    OutYear9 DOUBLE NULL DEFAULT 0.0,
    Sort TEXT(80) NULL DEFAULT NS,
    PRIMARY KEY(GrowthRatesId)
);