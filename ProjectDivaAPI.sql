USE [ProjectDivaAPI]
GO

DROP TABLE IF EXISTS Game
DROP TABLE IF EXISTS Song
DROP TABLE IF EXISTS Module

GO

CREATE TABLE Game
(
    GameID INT
        CONSTRAINT PK_GameID PRIMARY KEY
            IDENTITY(1, 1)              NOT NULL,
    [Name] VARCHAR(255)                 NOT NULL,
)

CREATE Table Song
(
    SongID INT
        CONSTRAINT PK_SongID PRIMARY KEY
            IDENTITY(1, 1)              NOT NULL,
    [Name] VARCHAR(50)                  NOT NULL,
    PVID   INT                          NOT NULL,
    Aura   VARCHAR(10)                  NULL,
)

CREATE TABLE Module
(
    ModuleID INT 
        CONSTRAINT PK_ModuleID PRIMARY KEY
            IDENTITY(1, 1)              NOT NULL,
    [Name] VARCHAR(50)                  NOT NULL,
    Aura   VARCHAR(10)                  NULL,
)