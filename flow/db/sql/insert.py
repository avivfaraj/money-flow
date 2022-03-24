import sqlite3
from sql.search import select_query
def new_person(conn, first_name, last_name, middle_name = ""):
    
    params = (first_name, middle_name, last_name)
    query = """INSERT INTO Person(firstName,middleName, lastName) VALUES(?,?,?);"""

    if not middle_name:
        query = """INSERT INTO Person(firstName, lastName) VALUES(?,?);"""
        params = (first_name, last_name)
    execute_query(conn = conn,
                query = query,
                params = params)


def new_bank(conn, account_id, bank_name, balance):
    banks_info = select_query(conn, """SELECT accountID, bankName FROM Bank;""",())
    if not (account_id, bank_name) in banks_info:
        execute_query(conn = conn,
                  query = """INSERT INTO Bank(accountID, bankName, balance) VALUES(?,?,?);""",
                  params = (account_id, bank_name, balance))
    else:
        raise ValueError("Bank is already exists in the system!")

def new_account_ownership(conn, person_id, account_id):
    execute_query(conn = conn,
                query = """INSERT INTO Ownership(personID, accountID) VALUES (?, ?);""",
                params = (person_id, account_id))


def new_card(conn, payment_id, account_id,company , type_, person_id):
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
    except Exception:
        conn.rollback()


def new_wire(conn, payment_id, account_id, company, person_id, recipient, sender, type_, details):
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
                    params = (person_id,payment_id))
    except Exception:
        conn.rollback()


## Not updated
def new_transaction(conn, 
                    details, 
                    sector,
                    t_type, 
                    quantity, 
                    unit_price,
                    discount,
                    payment_id):
    with conn:
        cur = conn.cursor()

        cur.execute("""SELECT paymentID FROM Payment;""")
        existing_ids = [id_[0] for id_ in cur.fetchall()]

        if payment_id in existing_ids:

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

    if isinstance(conn,sqlite3.Connection):
        conn.cursor().execute(query, params)

        if commit:
            conn.commit()
    else:
        raise TypeError("No connection to database") 


