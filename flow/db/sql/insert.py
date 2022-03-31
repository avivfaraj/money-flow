import sqlite3
from sql.search import select_query
def new_person(conn: "sqlite.Connection", first_name: str, last_name: str, middle_name: str = ""):
    '''
    Insert new person to the database

    Input:
    conn -> connection to sqlite3 database
    first_name, last_name -> name of the new person (str). Must have a value!
    middle_name -> can be null or an empty string.
    '''
    params = (first_name, middle_name, last_name)
    query = """INSERT INTO Person(firstName,middleName, lastName) VALUES(?,?,?);"""

    if not middle_name:
        query = """INSERT INTO Person(firstName, lastName) VALUES(?,?);"""
        params = (first_name, last_name)

    try:
        execute_query(conn = conn,
                query = query,
                params = params)

        print("Person inserted successfully")

    except TypeError as err:
        print("** Error **", err)

def new_bank(conn: "sqlite.Connection", account_id: int, bank_name: str, balance: float):
    '''
    Insert a new bank account

    Input:
    conn -> connection to sqlite3 database
    account_id -> 4 digits of bank account (int)
    bank_name -> Name of the bank (str)
    balance -> Current balance (float)
    '''
    banks_info = select_query(conn, """SELECT accountID, bankName FROM Bank;""",())
    if not (account_id, bank_name) in banks_info:

        try:
            execute_query(conn = conn,
                  query = """INSERT INTO Bank(accountID, bankName, balance) VALUES(?,?,?);""",
                  params = (account_id, bank_name, balance))

            print("Bank inserted successfully")

        except TypeError as err:
            print("** Error **", err)
    else:
        raise ValueError("Bank is already exist in the system!")

def new_account_ownership(conn: "sqlite.Connection", person_id: int, account_id: int):
    '''
    Add an owner to an existing bank account. 
    Both the owner and the bank account must be registered in the database.

    Input:
    conn -> connection to sqlite3 database
    person_id -> The auto-generated ID to identify the person (int)
    account_id -> 4 digits of bank account (int)
    '''

    try:
        execute_query(conn = conn,
                query = """INSERT INTO Ownership(personID, accountID) VALUES (?, ?);""",
                params = (person_id, account_id))

        print("New bank ownership added successfully")

    except TypeError as err:
        print("** Error **", err)

def new_card(conn: "sqlite.Connection",
             payment_id: int,
             account_id: int,
             company: str , 
             type_: str,
             person_id: int):
    '''
    Insert new card to database:  
    Payment -> Card -> Ownership

    Input:
    conn -> connection to sqlite3 database
    payment_id -> Last 4 digits of credit/debit card (int)
    account_id -> 4 digits of bank account (int)
    company -> Card's company (e.g. Mastercard, VISA)
    type_ -> Either "Debit" or "Credit"
    person_id -> The auto-generated ID to identify the person (int)
    '''

    # Ensure each query is executed without an exception
    try:
        execute_query(conn = conn,
                    query = """INSERT INTO Payment(paymentID, company, accountID) 
                               VALUES (?, ?, ?);""",
                    params = (payment_id, company, account_id),
                    commit = False)

        execute_query(conn = conn,
                    query = """INSERT INTO Card(cardID, cardType) 
                               VALUES (?, ?);""",
                    params = (payment_id, type_),
                    commit = False)

        execute_query(conn = conn,
                    query = """INSERT INTO Paym_Ownership(personID, payment_ID) 
                               VALUES ( ?, ?);""",
                    params = (person_id,payment_id))

        print("Card was inserted successfully")

    except TypeError as err:
        print("** Error **", err)

    # An error - Rollback  
    except Exception:
        print("An error occured while inserting a new card. Rolling back....")
        conn.rollback()
        print("Rollback Completed")


def new_wire(conn: "sqlite.Connection",
             payment_id: int,
             account_id: int, 
             company: str, 
             person_id: int, 
             recipient: str, 
             sender: str, 
             type_: str, 
             details: str):
    '''
    Insert new wire transfer to database:  
    Payment -> wire -> Ownership

    Input:
    conn -> connection to sqlite3 database
    payment_id -> Last 4 digits of credit/debit card (int)
    account_id -> 4 digits of bank account (int)
    company -> Card's company (e.g. Mastercard, VISA)
    person_id -> The auto-generated ID to identify the person (int)
    recipient -> Name of a person/company that receive the payment (str)
    sender -> Name of a person/company that send the payment (str)
    type_ -> Either "International" or "Domestic"
    details -> More information about this wire transfer (str).
    '''

    try:
        execute_query(conn = conn,
                    query = """INSERT INTO Payment(paymentID, company, accountID) 
                               VALUES (?, ?, ?);""",
                    params = (payment_id, company, account_id),
                    commit = False)

        execute_query(conn = conn,
                    query = """INSERT INTO Wire 
                               VALUES (?, ?, ?, ?, ?);""",
                    params = (payment_id,recipient, sender ,type_, details),
                    commit = False)

        execute_query(conn = conn,
                    query = """INSERT INTO Paym_Ownership(personID, payment_ID) 
                               VALUES ( ?, ?);""",
                    params = (person_id, payment_id))

        print("Wire transfer was inserted successfully")
    except TypeError as err:
        print("** Error **", err)

    # An error - Rollback 
    except Exception:
        print("An error occured while creating a new wire transfer. Rolling back....")
        conn.rollback()
        print("Rollback Completed")

def new_cheque(conn: "sqlite.Connection", 
               payment_id: int, 
               account_id: int, 
               company: str, 
               pay_to: str, 
               memo: str):
    '''
    Insert new cheque to database:  
    Payment -> Cheque

    Input:
    conn -> connection to sqlite3 database
    payment_id -> Last 4 digits of credit/debit card (int)
    account_id -> 4 digits of bank account (int)
    company -> Card's company (e.g. Mastercard, VISA)
    pay_to -> Name of person/company that deposit the cheque (str)
    memo -> Details regarding the payment (str)
    '''
    try:
        execute_query(conn = conn,
                    query = """INSERT INTO Payment(paymentID, company, accountID) 
                               VALUES (?, ?, ?);""",
                    params = (payment_id, company, account_id),
                    commit = False)

        execute_query(conn = conn,
                    query = """INSERT INTO Cheque 
                               VALUES (?, ?);""",
                    params = (pay_to,memo))

        print("New cheque was successfully inserted")
    except TypeError as err:
        print("** Error **", err)
    except Exception:
        conn.rollback()
        print("Rollback Completed")


def new_transaction(conn: "sqlite.Connection", 
                    details: str, 
                    sector: str,
                    t_type: str, 
                    quantity: int, 
                    unit_price: float,
                    discount: float,
                    payment_id: int):

    if isinstance(conn,sqlite3.Connection):
        cur = conn.cursor()

        # Fetch payment ID from database
        cur.execute("""SELECT * FROM Payment WHERE PaymentID = ?;""", (payment_id,))
        fetched = [id_[0] for id_ in cur.fetchall()]

        # Ensure payment exist
        if len(fetched) == 1:

            query = """INSERT INTO trans_details VALUES(NULL,?,?,?,?,?,?,?);"""

            params = (details,
                    sector, 
                    t_type, 
                    quantity, 
                    unit_price,
                    discount,
                    payment_id)
            cur.execute(query,params)

            conn.commit()

            return cur.lastrowid
        else:
            raise ValueError("Payment does not exist in DB!")


def execute_query(conn, query, params = (), commit = True):
    '''
    Execute one query using params as parameters (for update, insert etc.)
    commit can be False in order to run a few queries together.
    In this case, rollback can take place in case of an error.

    Input:
    conn -> connection to sqlite3 database
    query -> SQL query (str)
    params -> parameters for the query (tuple)
    commit -> Commit changes or wait to other SQL queries (Boolean) 
    '''

    if isinstance(conn,sqlite3.Connection):
        conn.cursor().execute(query, params)

        if commit:
            conn.commit()
    else:
        raise TypeError("No connection to database") 


