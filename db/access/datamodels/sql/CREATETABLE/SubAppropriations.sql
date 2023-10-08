CREATE TABLE SubAppropriations
(
	SubAppropriationsId AUTOINCREMENT NOT NULL UNIQUE,
	Code TEXT(150) NULL DEFAULT NS,
	Name TEXT(150) NULL DEFAULT NS,
	CONSTRAINT(SubAppropriationsPrimaryKey) 
		PRIMARY KEY(SubAppropriationsId )
);
