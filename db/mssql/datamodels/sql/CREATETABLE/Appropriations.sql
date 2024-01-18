CREATE TABLE Appropriations
(
	AppropriationsId INT           NOT NULL UNIQUE,
	Code             NVARCHAR(150) NULL DEFAULT ('NS'),
	Name             NVARCHAR(150) NULL DEFAULT ('NS'),
	CONSTRAINT AppropriationsPrimaryKey PRIMARY KEY
		(
		  AppropriationsId ASC
			)
);
