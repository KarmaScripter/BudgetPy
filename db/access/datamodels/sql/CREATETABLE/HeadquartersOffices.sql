CREATE TABLE HeadquartersOffices
(
	HeadquartersOfficesId     AUTOINCREMENT NOT NULL UNIQUE,
	ResourcePlanningOfficesId INT           NULL,
	Code                      TEXT( 150 )   NULL DEFAULT NS,
	Name                      TEXT( 150 )   NULL DEFAULT NS, CONSTRAINT
(
	HeadquartersOfficesPrimaryKey
)
	PRIMARY KEY
(
	HeadquartersOfficesId
)
	);
