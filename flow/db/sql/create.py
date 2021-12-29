import sqlite3
from sql.insert import execute_query

def create_tables(conn):
    with conn:
        create_person(conn)
        create_bank(conn)
        create_ownership(conn)
        create_card(conn)
        create_transaction(conn)
        create_payment_method(conn)
        create_variables(conn)

def create_person(conn):
    execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY,name TEXT)""",
                  params = ())

def create_bank(conn):

     execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS bank(
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL, 
                                    balance REAL DEFAULT 0);""")

def create_ownership(conn):


    execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS ownership(
                         id INTEGER PRIMARY KEY,
                         person_id INTEGER, 
                         account_id INTEGER,
                         FOREIGN KEY (person_id) 
                             REFERENCES person(id)
                                 ON DELETE SET NULL,
                         FOREIGN KEY (account_id) 
                             REFERENCES bank(id)
                                 ON DELETE SET NULL);""")

def create_card(conn):

        execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY,
                        person_id INTEGER,
                        account_id INTEGER,
                        company TEXT NOT NULL,
                        benefits TEXT DEFAULT '',
                        type TEXT DEFAULT 'Credit',
                        FOREIGN KEY(account_id) 
                            REFERENCES bank(id)
                                ON DELETE SET NULL,
                        FOREIGN KEY (person_id) 
                            REFERENCES person(id)
                                ON DELETE SET NULL)""")

def create_transaction(conn):

     execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS transaction_details(id INTEGER PRIMARY KEY,
                            account_id INTEGER,
                            payment_id INTEGER,
                            person_name TEXT, 
                            details TEXT,
                            sector TEXT,
                            type TEXT,
                            quantity INTEGER DEFAULT 1,
                            price MONEY NOT NULL,
                            FOREIGN KEY (account_id) REFERENCES bank(id)
                                ON DELETE SET NULL,
                            FOREIGN KEY (payment_id) REFERENCES payment_info(id)
                                ON DELETE SET NULL);""")

     execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS transaction_history(trans_id INTEGER PRIMARY KEY,
                            total MONEY,
                            balance MONEY DEFAULT NULL,
                            d_date DATE,
                            d_time TIME,
                            FOREIGN KEY (trans_id) REFERENCES transaction_details(id)
                                ON DELETE SET NULL);""")


def create_payment_method(conn):
    execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS payment_info(id INTEGER PRIMARY KEY,
                            method TEXT,
                            method_id INTEGER NOT NULL);""")


def create_variables(conn):
    execute_query(conn = conn,
                  query = """ CREATE TABLE IF NOT EXISTS _Variables(
                              id INTEGER PRIMARY KEY, 
                              diff MONEY);""")


    


