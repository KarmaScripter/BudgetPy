CREATE TABLE Reports
(
	ReportsId AUTOINCREMENT NOT NULL UNIQUE,
	Name      TEXT( 150 )   NULL DEFAULT NS,
	Title     TEXT( 150 )   NULL DEFAULT NS, CONSTRAINT
(
	ReportsPrimaryKey
)
	PRIMARY KEY
(
	ReportsId
)
	);
