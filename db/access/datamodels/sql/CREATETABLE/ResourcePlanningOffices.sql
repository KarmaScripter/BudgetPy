CREATE TABLE ResourcePlanningOffices
(
	ResourcePlanningOfficesId AUTOINCREMENT NOT NULL UNIQUE,
	Code TEXT(150) NULL DEFAULT NS,
	Name TEXT(150) NULL DEFAULT NS,
	CONSTRAINT(ResourcePlanningOfficesPrimaryKey) 
		PRIMARY KEY(ResourcePlanningOfficesId )
);
