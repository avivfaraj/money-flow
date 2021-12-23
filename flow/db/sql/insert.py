import sqlite3
def insert_person(conn, full_name):
  
    execute_query(conn = conn,
                  query = """INSERT INTO person(name) VALUES(?);""",
                  params = (full_name,))


def new_transaction(conn, 
                    bank_id, 
                    full_name, 
                    details, 
                    sector, 
                    payment_method, 
                    t_type, 
                    quantity, 
                    unit_price):
  if isinstance(conn,sqlite3.Connection):
    cur = conn.cursor()

    cur.execute("""SELECT id FROM bank;""")
    existing_ids = [id_[0] for id_ in cur.fetchall()]

    if bank_id in existing_ids:

      query = """INSERT INTO transaction_details VALUES(NULL,?,?,?,?,?,?,?,?);"""

      params = (bank_id, 
                full_name, 
                details,
                sector,
                payment_method, 
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


def execute_query(conn, query, params):

  if isinstance(conn,sqlite3.Connection):

    conn.cursor().execute(query, params)
    conn.commit()

  else:
    raise TypeError("No connection to database") 


