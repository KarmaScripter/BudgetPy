CREATE TABLE AccountingEvents
(
	AccountingEventsId INT NOT NULL UNIQUE,
	Code NVARCHAR(150) NULL DEFAULT ('NS'),
	Name NVARCHAR(150) NULL DEFAULT ('NS'),
	CONSTRAINT AccountingEventsPrimaryKey PRIMARY KEY
	(
		AccountsId ASC
	)
);
