import sqlite3
def insert_person(conn, full_name):
  
    execute_query(conn = conn,
                  query = """INSERT INTO person(name) VALUES(?);""",
                  params = (full_name,))


def new_transaction(conn, bank_id, full_name, details,
                    payment_method, t_type, quantity, unit_price):
    cur = conn.cursor()

    query = """INSERT INTO transaction_details VALUES(NULL,?,?,?,?,?,?,?);"""

    params = (bank_id, 
              full_name, 
              details,
              payment_method, 
              t_type, 
              quantity, 
              unit_price)
    
    cur.execute(query,params)

    conn.commit()

    return cur.lastrowid


def execute_query(conn, query, params):

  if isinstance(conn,sqlite3.Connection):

    conn.cursor().execute(query, params)
    conn.commit()

  else:
    raise TypeError("No connection to database") 


