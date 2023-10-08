CREATE TABLE CompassErrors
(
	CompassErrorsId INT NOT NULL UNIQUE,
	Code NVARCHAR(150) NULL DEFAULT ('NS'),
	Message NVARCHAR(150) NULL DEFAULT ('NS'),
	Severity NVARCHAR(150) NULL DEFAULT ('NS'),
	CONSTRAINT CompassErrorsPrimaryKey PRIMARY KEY
	(
		CompassErrorsId ASC
	)
);
