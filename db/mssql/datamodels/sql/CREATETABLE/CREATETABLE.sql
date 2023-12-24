CREATE TABLE TableName
(
	TableNameId INT NOT NULL UNIQUE,
	FieldName NVARCHAR(150) NULL DEFAULT ('NS'),
	NumericName DOUBLE NULL DEFAULT (0.0),
	CONSTRAINT TableNamePrimaryKey PRIMARY KEY
	(
		TableNameId  ASC
	)
);
