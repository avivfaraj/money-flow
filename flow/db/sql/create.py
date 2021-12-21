import sqlite3

def create_tables(cursor):
    if isinstance(cursor, sqlite3.Cursor):
        create_person(cursor)
        create_bank(cursor)
        create_ownership(cursor)
        create_card(cursor)
        create_transaction(cursor)
    else:
        raise TypeError("Invalid sqlite3 cursor")

def create_person(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY,name TEXT)""")


def create_bank(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS bank(
                                    id INTEGER PRIMARY KEY,
                                    name TEXT, 
                                    balance REAL)""")


def create_ownership(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS ownership(
                         id INTEGER PRIMARY KEY,
                         person_id INTEGER, 
                         account_id INTEGER,
                         FOREIGN KEY (person_id) 
                             REFERENCES person(id)
                                 ON DELETE SET NULL,
                         FOREIGN KEY (account_id) 
                             REFERENCES bank(id)
                                 ON DELETE SET NULL)""")
def create_card(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY,
                        person_id INTEGER,
                        account_id INTEGER,
                        company TEXT,
                        benefits TEXT,
                        type TEXT,
                        FOREIGN KEY(account_id) 
                            REFERENCES bank(id)
                                ON DELETE SET NULL,
                        FOREIGN KEY (person_id) 
                            REFERENCES person(id)
                                ON DELETE SET NULL)""")

def create_transaction(cursor):
    cursor.executescript("""CREATE TABLE IF NOT EXISTS transactions(id INTEGER PRIMARY KEY,
                            account_id INTEGER,
                            person_name TEXT, 
                            details TEXT,
                            method TEXT,
                            type TEXT,
                            quantity INTEGER,
                            price MONEY,
                            total MONEY ALWAYS AS (quantity * price) STORED,
                            balance MONEY DEFAULT NULL,
                            d_date DATE,
                            d_time TIME,
                            FOREIGN KEY (account_id) REFERENCES bank(id)
                                ON DELETE SET NULL);
                            """)


    


