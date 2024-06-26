CREATE TABLE ColumnSchema
(
	ColumnSchemaId AUTOINCREMENT NOT NULL UNIQUE,
	DataType       TEXT( 150 )   NULL DEFAULT NS,
	ColumnName     TEXT( 150 )   NULL DEFAULT NS,
	TableName      TEXT( 150 )   NULL DEFAULT NS,
	ColumnCaption  TEXT( 150 )   NULL DEFAULT NS, CONSTRAINT
(
	ColumnSchemaPrimaryKey
)
	PRIMARY KEY
(
	ColumnSchemaId
)
	);
