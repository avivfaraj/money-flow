--
-- File generated with SQLiteStudio v3.3.3 on Thu Mar 24 18:09:38 2022
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: _Variables
DROP TABLE IF EXISTS _Variables;

CREATE TABLE _Variables (
    total  DOUBLE,
    bankID INTEGER REFERENCES Bank (accountID) 
);


-- Table: Bank
DROP TABLE IF EXISTS Bank;

CREATE TABLE Bank (
    accountID INTEGER CONSTRAINT bank_pk PRIMARY KEY ASC ON CONFLICT ROLLBACK AUTOINCREMENT,
    bankName  TEXT    NOT NULL,
    balance   DOUBLE  DEFAULT (0) 
);


-- Table: Benefits
DROP TABLE IF EXISTS Benefits;

CREATE TABLE Benefits (
    cardID    INTEGER CONSTRAINT benefits_fk1 REFERENCES Card (cardID) ON DELETE CASCADE
                                                                       ON UPDATE RESTRICT
                      NOT NULL,
    benefitID INTEGER NOT NULL,
    details   TEXT    NOT NULL,
    CONSTRAINT benefits_pk PRIMARY KEY (
        cardID,
        benefitID ASC
    )
    ON CONFLICT ROLLBACK
);


-- Table: Card
DROP TABLE IF EXISTS Card;

CREATE TABLE Card (
    cardID    INTEGER CONSTRAINT card_pk PRIMARY KEY ON CONFLICT ROLLBACK
                      CONSTRAINT card_fk1 REFERENCES Payment (paymentID) ON DELETE CASCADE
                                                                         ON UPDATE RESTRICT,
    cardType  TEXT    DEFAULT ('Debit'),
    ownerName         NOT NULL
);


-- Table: Cheque
DROP TABLE IF EXISTS Cheque;

CREATE TABLE Cheque (
    chequeID INTEGER PRIMARY KEY
                     CONSTRAINT cheque_fk REFERENCES Payment (paymentID) ON DELETE CASCADE
                                                                         ON UPDATE RESTRICT,
    payTo    TEXT    NOT NULL,
    memo     TEXT    NOT NULL
);


-- Table: Ownership
DROP TABLE IF EXISTS Ownership;

CREATE TABLE Ownership (
    personID  INTEGER CONSTRAINT ownership_fk1 REFERENCES Person (personID) ON DELETE CASCADE
                                                                            ON UPDATE RESTRICT
                                                                            MATCH SIMPLE
                      NOT NULL,
    accountID INTEGER CONSTRAINT ownership_fk2 REFERENCES Bank (accountID) ON DELETE CASCADE
                                                                           ON UPDATE RESTRICT
                                                                           MATCH SIMPLE
                      NOT NULL,
    CONSTRAINT ownership_pk PRIMARY KEY (
        personID ASC,
        accountID ASC
    )
    ON CONFLICT ROLLBACK
);


-- Table: Paym_Ownership
DROP TABLE IF EXISTS Paym_Ownership;

CREATE TABLE Paym_Ownership (
    personID   INTEGER CONSTRAINT hold_fk1 REFERENCES Person (personID) ON DELETE CASCADE
                                                                        ON UPDATE RESTRICT
                       NOT NULL,
    payment_ID INTEGER CONSTRAINT hold_fk2 REFERENCES Payment (paymentID) ON DELETE CASCADE
                                                                          ON UPDATE RESTRICT
                       NOT NULL,
    CONSTRAINT hold_pk PRIMARY KEY (
        personID ASC,
        payment_ID ASC
    )
    ON CONFLICT ROLLBACK
);


-- Table: Payment
DROP TABLE IF EXISTS Payment;

CREATE TABLE Payment (
    paymentID INTEGER CONSTRAINT payment_pk PRIMARY KEY ASC ON CONFLICT ROLLBACK,
    company   TEXT    NOT NULL
                      CHECK (company IN ('Bank of America', 'Capital One', 'Charles Schwab', 'Chase', 'AMEX', 'Mastercard', 'Visa') ),
    accountID INTEGER CONSTRAINT payment_fk1 REFERENCES Bank (accountID) ON DELETE CASCADE
                                                                         ON UPDATE RESTRICT
);


-- Table: Person
DROP TABLE IF EXISTS Person;

CREATE TABLE Person (
    personID   INTEGER CONSTRAINT person_pk PRIMARY KEY ASC ON CONFLICT ROLLBACK AUTOINCREMENT,
    firstName  TEXT    NOT NULL,
    middleName TEXT    DEFAULT (''),
    lastName   TEXT    NOT NULL
);


-- Table: trans_details
DROP TABLE IF EXISTS trans_details;

CREATE TABLE trans_details (
    transID   INTEGER CONSTRAINT trans_details_pk PRIMARY KEY ASC ON CONFLICT ROLLBACK AUTOINCREMENT,
    details   TEXT    NOT NULL,
    sector    TEXT    DEFAULT (''),
    type      TEXT,
    quantity  INTEGER DEFAULT (1),
    price     DOUBLE  NOT NULL,
    discount  DOUBLE  DEFAULT (0),
    paymentID INTEGER CONSTRAINT trans_details_fk1 REFERENCES Payment (paymentID) ON DELETE CASCADE
                                                                                  ON UPDATE RESTRICT
);


-- Table: trans_history
DROP TABLE IF EXISTS trans_history;

CREATE TABLE trans_history (
    transID    INTEGER CONSTRAINT trans_history_fk REFERENCES trans_details (transID) ON DELETE CASCADE
                                                                                      ON UPDATE RESTRICT
                       CONSTRAINT trans_history_pk PRIMARY KEY ASC ON CONFLICT ROLLBACK,
    total      DOUBLE  NOT NULL,
    balance    DOUBLE  NOT NULL,
    trans_date DATE    DEFAULT (DATE('now') ),
    trans_time TIME    DEFAULT (TIME('now') ) 
);


-- Table: Wire
DROP TABLE IF EXISTS Wire;

CREATE TABLE Wire (
    wireID    INTEGER PRIMARY KEY
                      CONSTRAINT wire_fk REFERENCES Payment (paymentID) ON DELETE CASCADE
                                                                        ON UPDATE RESTRICT,
    recipient TEXT    NOT NULL,
    sender    TEXT    NOT NULL,
    type      TEXT    CHECK (type IN ('Domestic', 'International') ) 
                      NOT NULL,
    details   TEXT    NOT NULL
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
