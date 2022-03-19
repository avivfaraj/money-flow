import sqlite3
from sql.insert import execute_query

def create_tables(conn):
    with conn:
        execute_query(conn, "PRAGMA foreign_keys = OFF;", ())
        create_person(conn)
        create_bank(conn)
        create_ownership(conn)
        create_card(conn)
        create_transaction(conn)
        create_payment_method(conn)
        create_variables(conn)
        execute_query(conn, "PRAGMA foreign_keys = ON;", ())


def create_person(conn):
    execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS Person(personID   INTEGER CONSTRAINT person_pk PRIMARY KEY ASC ON CONFLICT ROLLBACK AUTOINCREMENT,
                                                               firstName  TEXT    NOT NULL,
                                                               middleName TEXT    DEFAULT (''),
                                                               lastName   TEXT    NOT NULL
                                                               );""",
                  params = ())

def create_bank(conn):

     execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS Bank(
                                    accountID INTEGER CONSTRAINT bank_pk PRIMARY KEY ASC ON CONFLICT ROLLBACK AUTOINCREMENT,
                                    bankName  TEXT    NOT NULL,
                                    balance   DOUBLE  DEFAULT (0));""")
def create_ownership(conn):


    execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS Ownership(
                         personID  INTEGER CONSTRAINT ownership_fk1 REFERENCES Person (personID) ON DELETE CASCADE
                                                                            ON UPDATE RESTRICT
                                                                            MATCH SIMPLE
                                                                            NOT NULL,
                         
                         accountID INTEGER CONSTRAINT ownership_fk2 REFERENCES Bank (accountID) ON DELETE CASCADE
                                                                            ON UPDATE RESTRICT
                                                                            MATCH SIMPLE
                                                                            NOT NULL,
                        CONSTRAINT ownership_pk PRIMARY KEY (personID ASC, accountID ASC)
                                                            ON CONFLICT ROLLBACK);""")

def create_card(conn):

        execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS Card(cardID   INTEGER CONSTRAINT card_pk PRIMARY KEY ON CONFLICT ROLLBACK
                     CONSTRAINT card_fk1 REFERENCES Payment (paymentID) ON DELETE CASCADE
                                                                        ON UPDATE RESTRICT,
                                cardType TEXT    DEFAULT ('Debit') 
                            );""")

def create_transaction(conn):

     execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS trans_details(transID   INTEGER CONSTRAINT trans_details_pk PRIMARY KEY ASC ON CONFLICT ROLLBACK AUTOINCREMENT,
    details   TEXT    NOT NULL,
    sector    TEXT    DEFAULT (''),
    type      TEXT,
    quantity  INTEGER DEFAULT (1),
    price     DOUBLE  NOT NULL,
    discount  DOUBLE  DEFAULT (0),
    paymentID INTEGER CONSTRAINT trans_details_fk1 REFERENCES Payment (paymentID) ON DELETE CASCADE
                                                                                  ON UPDATE RESTRICT
);""")

     execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS trans_history(transID    INTEGER CONSTRAINT trans_history_fk REFERENCES trans_details (transID) ON DELETE CASCADE
                                                                                      ON UPDATE RESTRICT
                       CONSTRAINT trans_history_pk PRIMARY KEY ASC ON CONFLICT ROLLBACK,
    total      DOUBLE  NOT NULL,
    balance    DOUBLE  NOT NULL,
    trans_date DATE    DEFAULT (DATE('now') ),
    trans_time TIME    DEFAULT (TIME('now') ) 
);
""")


def create_payment_method(conn):
    execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS Payment(paymentID INTEGER CONSTRAINT payment_pk PRIMARY KEY ASC ON CONFLICT ROLLBACK,
    company   TEXT    NOT NULL
                      CHECK (company IN ('Bank of America', 'Capital One', 'Charles Schwab', 'Chase', 'AMEX', 'Mastercard', 'Visa') ),
    accountID INTEGER CONSTRAINT payment_fk1 REFERENCES Bank (accountID) ON DELETE CASCADE
                                                                         ON UPDATE RESTRICT
);""")

    execute_query(conn = conn,
                  query = """

CREATE TABLE IF NOT EXISTS Paym_Ownership(personID   INTEGER CONSTRAINT hold_fk1 REFERENCES Person (personID) ON DELETE CASCADE
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
);""")


def create_variables(conn):
    execute_query(conn = conn,
                  query = """ CREATE TABLE IF NOT EXISTS _Variables(
                              total  DOUBLE,
    bankID INTEGER REFERENCES Bank (accountID) 
);""")


    


