CREATE TABLE IF NOT EXISTS "WorkCodes" 
(
    "WorkCodesId" INTEGER NOT NULL UNIQUE,
    "Code" TEXT(80) NULL DEFAULT 'NS',
    "Name" TEXT(80) NULL DEFAULT 'NS',
    PRIMARY KEY ("WorkCodesId" AUTOINCREMENT)
);