CREATE TABLE Documents 
(
    DocumentsId INTEGER NOT NULL UNIQUE,
    Code TEXT(80) NULL DEFAULT NS,
    Category TEXT(80) NULL DEFAULT NS,
    Name TEXT(80) NULL DEFAULT NS,
    System TEXT(80) NULL DEFAULT NS,
    PRIMARY KEY(DocumentsId)
);