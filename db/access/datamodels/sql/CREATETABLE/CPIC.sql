CREATE TABLE CPIC 
(
    CpicId INTEGER NOT NULL UNIQUE,
    Type TEXT(80) NULL DEFAULT NS,
    Code TEXT(80) NULL DEFAULT NS,
    Name TEXT(80) NULL DEFAULT NS,
    PRIMARY KEY(CpicId)
);