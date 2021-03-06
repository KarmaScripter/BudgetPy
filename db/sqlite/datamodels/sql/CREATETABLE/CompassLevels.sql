CREATE TABLE IF NOT EXISTS "CompassLevels" 
(
	"CompassLevelsId"	INTEGER NOT NULL UNIQUE,
	"BudgetLevel"	TEXT(80) NULL DEFAULT 'NS',
	"BFY"	TEXT(80) NULL DEFAULT 'NS',
	"EFY"	TEXT(80) NULL DEFAULT 'NS',
	"FundCode"	TEXT(80) NULL DEFAULT 'NS',
	"FundName"	TEXT(80) NULL DEFAULT 'NS',
	"AppropriationCode"	TEXT(80) NULL DEFAULT 'NS',
	"SubAppropriationCode"	TEXT(80) NULL DEFAULT 'NS',
	"AppropriationName"	TEXT(80) NULL DEFAULT 'NS',
	"TreasurySymbol"	TEXT(80) NULL DEFAULT 'NS',
	"DocumentType"	TEXT(80) NULL DEFAULT 'NS',
	"LowerName"	TEXT(80) NULL DEFAULT 'NS',
	"PostedControlFlag"	TEXT(80) NULL DEFAULT 'NS',
	"ActualRecoveryTransType"	TEXT(80) NULL DEFAULT 'NS',
	"CommitmentSpendControlFlag"	TEXT(80) NULL DEFAULT 'NS',
	"BudgetDefault"	TEXT(80) NULL DEFAULT 'NS',
	"LowerChildExpendSpendCtrlFlag"	TEXT(80) NULL DEFAULT 'NS',
	"LowerChildExpenseSpendCtrlFlag"	TEXT(80) NULL DEFAULT 'NS',
	"FteControlFlag"	TEXT(80) NULL DEFAULT 'NS',
	"AccrualSpendingControlFlag"	TEXT(80) NULL DEFAULT 'NS',
	"ObligationSpendingControlFlag"	TEXT(80) NULL DEFAULT 'NS',
	"PreCommitmentSpendingControlFlag"	TEXT(80) NULL DEFAULT 'NS',
	"LowerCommSpendCtrlFlag"	TEXT(80) NULL DEFAULT 'NS',
	"LowerObligSpendCtrlFlag"	TEXT(80) NULL DEFAULT 'NS',
	"LowerExpenditureSpendingCtrlFlag"	TEXT(80) NULL DEFAULT 'NS',
	"LowerExpenseSpendingCtrlFlag"	TEXT(80) NULL DEFAULT 'NS',
	"LowerPostedCtrlFlag"	TEXT(80) NULL DEFAULT 'NS',
	"LowerPostedTransType"	TEXT(80) NULL DEFAULT 'NS',
	"LowerTransType"	TEXT(80) NULL DEFAULT 'NS',
	"LowerPostedFlag"	TEXT(80) NULL DEFAULT 'NS',
	"LowerPreCommSpendCtrlFlag"	TEXT(80) NULL DEFAULT 'NS',
	"LowerRecoveriesSpendingOption"	TEXT(80) NULL DEFAULT 'NS',
	"LowerRecoveriesOption"	TEXT(80) NULL DEFAULT 'NS',
	"LowerReimbSpendingOption"	TEXT(80) NULL DEFAULT 'NS',
	"Date"	TEXT(80) NULL DEFAULT 'NS',
	"TotalAuthority"	NUMERIC NULL DEFAULT 0,
	"OriginalAmount"	NUMERIC NULL DEFAULT 0,
	"CarryoverAvailabilityPercentage"	NUMERIC NULL DEFAULT 0,
	"CarryIn"	NUMERIC NULL DEFAULT 0,
	"CarryOut"	NUMERIC NULL DEFAULT 0,
	"FundsIn"	NUMERIC NULL DEFAULT 0,
	"FundOut"	NUMERIC NULL DEFAULT 0,
	"RecoveriesWithdrawn"	NUMERIC NULL DEFAULT 0,
	"ActualRecoveries"	NUMERIC NULL DEFAULT 0,
	"ActualReimbursements"	NUMERIC NULL DEFAULT 0,
	"AgreementReimbursables"	NUMERIC NULL DEFAULT 0,
	PRIMARY KEY("CompassLevelsId" AUTOINCREMENT)
);