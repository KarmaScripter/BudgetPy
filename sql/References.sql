BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Divisions" (
	"DivisionId"	INTEGER NOT NULL UNIQUE,
	"Code"	TEXT(255) NOT NULL,
	"Name"	TEXT(255),
	"Caption"	TEXT(255),
	"Title"	TEXT(255),
	"FCO"	TEXT(255),
	"Icon"	TEXT(255),
	"Logo"	TEXT(255),
	CONSTRAINT "PrimaryKeyDivisions" PRIMARY KEY("DivisionId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Accounts" (
	"AccountId"	INTEGER NOT NULL UNIQUE,
	"Code"	TEXT(255) NOT NULL,
	"ActivityCode"	TEXT(255),
	"Name"	TEXT(255),
	"Title"	TEXT(255),
	"ProgramAreaCode"	TEXT(255),
	"ProgramProjectCode"	TEXT(255),
	"GoalCode"	TEXT(255),
	"ObjectiveCode"	TEXT(255),
	CONSTRAINT "PrimaryKeyAccounts" PRIMARY KEY("AccountId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "FinanceObjectClasses" (
	"FinanceObjectClassId"	INTEGER NOT NULL UNIQUE,
	"Code"	TEXT(255) NOT NULL,
	"Name"	TEXT(255),
	CONSTRAINT "PrimaryKeyFinanceObjectClasses" PRIMARY KEY("FinanceObjectClassId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "FiscalYears" (
	"FiscalYearId"	INTEGER NOT NULL UNIQUE,
	"BFY"	TEXT(255) NOT NULL,
	"EFY"	TEXT(255),
	"FirstYear"	TEXT(255),
	"LastYear"	TEXT(255),
	"ExpiringYear"	TEXT(255),
	"StartDate"	DATETIME,
	"EndDate"	DATETIME,
	"Availability"	TEXT(255),
	"Columbus"	DATETIME,
	"Thanksgiving"	DATETIME,
	"Christmas"	DATETIME,
	"NewYears"	DATETIME,
	"MartinLutherKing"	DATETIME,
	"Presidents"	DATETIME,
	"Memorial"	DATETIME,
	"Veterans"	DATETIME,
	"Labor"	DATETIME,
	"WorkDays"	DOUBLE,
	"WeekDays"	DOUBLE,
	"WeekEnds"	DOUBLE,
	CONSTRAINT "PrimaryKeyFiscalYears" PRIMARY KEY("FiscalYearId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Funds" (
	"FundId"	INTEGER NOT NULL UNIQUE,
	"Code"	TEXT(255) NOT NULL,
	"Name"	TEXT(255),
	"TreasurySymbol"	TEXT(255),
	"Title"	TEXT(255),
	CONSTRAINT "PrimaryKeyFunds" PRIMARY KEY("FundId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Goals" (
	"GoalId"	INTEGER NOT NULL UNIQUE,
	"Code"	TEXT(255),
	"Name"	TEXT(255),
	"Title"	TEXT(255),
	CONSTRAINT "PrimaryKeyGoals" PRIMARY KEY("GoalId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ProgramProjects" (
	"ProgramProjectId"	INTEGER NOT NULL UNIQUE,
	"Code"	TEXT(255) NOT NULL,
	"Name"	TEXT(255),
	"Title"	TEXT(255),
	"Laws"	TEXT(255),
	"Narrative"	TEXT(255),
	"Definition"	TEXT(255),
	"ProgramAreaCode"	TEXT(255),
	"ProgramAreaName"	TEXT(255),
	CONSTRAINT "PrimaryKeyProgramProjects" PRIMARY KEY("ProgramProjectId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ResourcePlanningImplementationOffices" (
	"RpioId"	INTEGER NOT NULL UNIQUE,
	"Code"	TEXT(255),
	"Name"	TEXT(255),
	CONSTRAINT "PrimaryKeyResourcePlanningImplementationOffices" PRIMARY KEY("RpioId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ResponsibilityCenters" (
	"ResponsibilityCenterId"	INTEGER NOT NULL UNIQUE,
	"Code"	TEXT(255),
	"Name"	TEXT(255),
	"Title"	TEXT(255),
	CONSTRAINT "PrimaryKeyResponsibilityCenters" PRIMARY KEY("ResponsibilityCenterId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Activities" (
	"ActivityId"	INTEGER NOT NULL UNIQUE,
	"Code"	TEXT(255) NOT NULL,
	"Name"	TEXT(255),
	"Title"	TEXT(255),
	CONSTRAINT "PrimaryKeyActivities" PRIMARY KEY("ActivityId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "AllowanceHolders" (
	"AllowanceHolderId"	INTEGER NOT NULL UNIQUE,
	"Code"	TEXT(255) NOT NULL,
	"Name"	TEXT(255),
	CONSTRAINT "PrimaryKeyAllowanceHolders" PRIMARY KEY("AllowanceHolderId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Appropriations" (
	"AppropriationId"	INTEGER NOT NULL UNIQUE,
	"BFY"	TEXT(255) NOT NULL,
	"Title"	TEXT(255),
	"PublicLaw"	TEXT(255),
	"EnactedDate"	DATETIME,
	CONSTRAINT "PrimaryKeyAppropriations" PRIMARY KEY("AppropriationId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "BudgetObjectClasses" (
	"BudgetObjectClassId"	INTEGER NOT NULL UNIQUE,
	"Code"	TEXT(255) NOT NULL,
	"Name"	TEXT(255),
	CONSTRAINT "PrimaryKeyBudgetObjectClasses" PRIMARY KEY("BudgetObjectClassId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CPIC" (
	"CpicId"	INTEGER NOT NULL UNIQUE,
	"Code"	TEXT(255) NOT NULL,
	"CostAreaCode"	TEXT(255),
	"CostAreaName"	TEXT(255),
	"ProjectCode"	TEXT(255),
	"ProjectName"	TEXT(255),
	CONSTRAINT "PrimaryKeyCPIC" PRIMARY KEY("CpicId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ProgramAreas" (
	"ProgramAreaId"	INTEGER NOT NULL UNIQUE,
	"Code"	TEXT(255) NOT NULL,
	"Name"	TEXT(255),
	CONSTRAINT "PrimaryKeyProgramAreas" PRIMARY KEY("ProgramAreaId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "GsPayScale" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"LOCNAME"	TEXT(255),
	"GRADE"	DOUBLE,
	"ANNUAL1"	DOUBLE,
	"HOURLY1"	TEXT(255),
	"OVERTIME1"	TEXT(255),
	"ANNUAL2"	DOUBLE,
	"HOURLY2"	TEXT(255),
	"OVERTIME2"	TEXT(255),
	"ANNUAL3"	DOUBLE,
	"HOURLY3"	TEXT(255),
	"OVERTIME3"	TEXT(255),
	"ANNUAL4"	DOUBLE,
	"HOURLY4"	TEXT(255),
	"OVERTIME4"	TEXT(255),
	"ANNUAL5"	DOUBLE,
	"HOURLY5"	TEXT(255),
	"OVERTIME5"	TEXT(255),
	"ANNUAL6"	DOUBLE,
	"HOURLY6"	TEXT(255),
	"OVERTIME6"	TEXT(255),
	"ANNUAL7"	DOUBLE,
	"HOURLY7"	TEXT(255),
	"OVERTIME7"	TEXT(255),
	"ANNUAL8"	DOUBLE,
	"HOURLY8"	TEXT(255),
	"OVERTIME8"	TEXT(255),
	"ANNUAL9"	DOUBLE,
	"HOURLY9"	TEXT(255),
	"OVERTIME9"	TEXT(255),
	"ANNUAL10"	DOUBLE,
	"HOURLY10"	TEXT(255),
	"OVERTIME10"	TEXT(255),
	CONSTRAINT "PrimaryKeyGsPayScale" PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Holidays" (
	"HolidayId"	INTEGER NOT NULL UNIQUE,
	"ColumbusDay"	DATETIME,
	"ThanksgivingDay"	DATETIME,
	"ChristmasDay"	DATETIME,
	"NewYearsDay"	DATETIME,
	"MartinLutherKingDay"	DATETIME,
	"PresidentsDay"	DATETIME,
	"MemorialDay"	DATETIME,
	"VeteransDay"	DATETIME,
	"LaborDay"	DATETIME,
	CONSTRAINT "PrimaryKeyHoldiays" PRIMARY KEY("HolidayId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Messages" (
	"MessageId"	INTEGER NOT NULL UNIQUE,
	"Message"	TEXT(255),
	"Type"	TEXT(255),
	"Form"	TEXT(255),
	CONSTRAINT "PrimaryKeyMessages" PRIMARY KEY("MessageId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "NationalPrograms" (
	"NationalProgramId"	INTEGER NOT NULL UNIQUE,
	"Code"	TEXT(255) NOT NULL,
	"Name"	TEXT(255),
	"RpioCode"	TEXT(255),
	"Title"	TEXT(255),
	CONSTRAINT "PrimaryKeyNationalPrograms" PRIMARY KEY("NationalProgramId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Organizations" (
	"OrganizationId"	INTEGER NOT NULL UNIQUE,
	"Code"	TEXT(255) NOT NULL,
	"Name"	TEXT(255),
	CONSTRAINT "PrimaryKeyOrganizations" PRIMARY KEY("OrganizationId" AUTOINCREMENT)
);
COMMIT;
