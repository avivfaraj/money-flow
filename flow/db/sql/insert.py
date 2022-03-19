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
    execute_query(conn = conn,
                query = """INSERT INTO Payment(paymentID, company, accountID) 
                           VALUES (?, ?, ?);""",
                params = (payment_id, company, account_id))

    execute_query(conn = conn,
                query = """INSERT INTO Card(cardID, cardType) 
                           VALUES (?, ?);""",
                params = (payment_id, type_))

    execute_query(conn = conn,
                query = """INSERT INTO Paym_Ownership(personID, payment_ID) 
                           VALUES ( ?, ?);""",
                params = (person_id,payment_id))


## Not updated
def new_transaction(conn, 
                    bank_id,
                    method,
                    method_id,
                    full_name, 
                    details, 
                    sector,
                    t_type, 
                    quantity, 
                    unit_price):
    if isinstance(conn,sqlite3.Connection):
        cur = conn.cursor()

        cur.execute("""SELECT id FROM bank;""")
        existing_ids = [id_[0] for id_ in cur.fetchall()]

        if bank_id in existing_ids:
          
            cur.execute("""SELECT method, method_id 
                         FROM payment_info;""")
            rowid = -1

            if not (method, method_id) in cur.fetchall():
                execute_query(conn = conn,
                          query = "INSERT INTO payment_info(method, method_id) VALUES (?, ?);",
                          params = (method, method_id))
                rowid = cur.execute("SELECT MAX(id) FROM payment_info;").fetchone()[0]
            else:
                if method == "Credit":
                    rowid = cur.execute("""SELECT id FROM payment_info
                                     WHERE method_id = ?;""", (method_id, )).fetchone()[0]


            query = """INSERT INTO transaction_details VALUES(NULL,?,?,?,?,?,?,?,?);"""

            params = (bank_id,
                    rowid,
                    full_name, 
                    details,
                    sector, 
                    t_type, 
                    quantity, 
                    unit_price)
            cur.execute(query,params)

            conn.commit()

            return cur.lastrowid
        else:
            raise ValueError("Bank ID does not exist!")
    else:
        raise TypeError("No connection to database")


def execute_query(conn, query, params = ()):

    if isinstance(conn,sqlite3.Connection):

        conn.cursor().execute(query, params)
        conn.commit()

    else:
        raise TypeError("No connection to database") 


