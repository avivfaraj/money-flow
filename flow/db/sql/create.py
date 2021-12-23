import sqlite3
from sql.insert import execute_query

def create_tables(conn):
    with conn:
        create_person(conn)
        create_bank(conn)
        create_ownership(conn)
        create_card(conn)
        create_transaction(conn)

def create_person(conn):
    execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY,name TEXT)""",
                  params = ())

def create_bank(conn):

     execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS bank(
                                    id INTEGER PRIMARY KEY,
                                    name TEXT, 
                                    balance REAL);""",
                  params = ())

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
                                 ON DELETE SET NULL);""",
                  params = ())

def create_card(conn):

        execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY,
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
                                ON DELETE SET NULL)""",
                  params = ())

def create_transaction(conn):

     execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS transaction_details(id INTEGER PRIMARY KEY,
                            account_id INTEGER,
                            person_name TEXT, 
                            details TEXT,
                            sector TEXT,
                            method TEXT,
                            type TEXT,
                            quantity INTEGER,
                            price MONEY,
                            FOREIGN KEY (account_id) REFERENCES bank(id)
                                ON DELETE SET NULL);""",
                  params = ())

     execute_query(conn = conn,
                  query = """CREATE TABLE IF NOT EXISTS transaction_history(trans_id INTEGER PRIMARY KEY,
                            total MONEY,
                            balance MONEY DEFAULT NULL,
                            d_date DATE,
                            d_time TIME,
                            FOREIGN KEY (trans_id) REFERENCES transaction_details(id)
                                ON DELETE SET NULL);""",
                  params = ())

    


