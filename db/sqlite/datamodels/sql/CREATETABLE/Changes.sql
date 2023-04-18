CREATE TABLE IF NOT EXISTS Changes 
(
	ChangesId	INTEGER NOT NULL,
	TableName	TEXT(80) NULL DEFAULT 'NS',
	FieldName	TEXT(80) NULL DEFAULT 'NS',
	Action	TEXT(80) NULL DEFAULT 'NS',
	OldValue	TEXT(80) NULL DEFAULT 'NS',
	NewValue	TEXT(80) NULL DEFAULT 'NS',
	TimeStamp	datetime NULL,
	Message	TEXT(80) NULL DEFAULT 'NS',
	PRIMARY KEY(ChangesId AUTOINCREMENT)
);