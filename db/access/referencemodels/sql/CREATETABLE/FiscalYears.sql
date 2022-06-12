CREATE TABLE FiscalYears 
(
    FiscalYearsId INTEGER NOT NULL UNIQUE,
    BFY TEXT(80) NULL DEFAULT NS,
    EFY TEXT(80) NULL DEFAULT NS,
    StartDate TEXT(80) NULL DEFAULT NS,
    Columbus TEXT(80) NULL DEFAULT NS,
    Veterans TEXT(80) NULL DEFAULT NS,
    Thanksgiving TEXT(80) NULL DEFAULT NS,
    Christmas TEXT(80) NULL DEFAULT NS,
    NewYears TEXT(80) NULL DEFAULT NS,
    MartinLutherKing TEXT(80) NULL DEFAULT NS,
    Presidents TEXT(80) NULL DEFAULT NS,
    Memorial TEXT(80) NULL DEFAULT NS,
    Juneteenth TEXT(80) NULL DEFAULT NS,
    Independence TEXT(80) NULL DEFAULT NS,
    Labor TEXT(80) NULL DEFAULT NS,
    ExpiringYear TEXT(80) NULL DEFAULT NS,
    ExpirationDate TEXT(80) NULL DEFAULT NS,
    WorkDays TEXT(80) NULL DEFAULT NS,
    WeekDays TEXT(80) NULL DEFAULT NS,
    WeekEnds TEXT(80) NULL DEFAULT NS,
    EndDate TEXT(80) NULL DEFAULT NS,
    Availability TEXT(80) NULL DEFAULT NS,
    PRIMARY KEY(FiscalYearsId)
);