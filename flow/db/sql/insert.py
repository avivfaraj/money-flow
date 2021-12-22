def insert_person(cursor, full_name):
    if cursor:
        cursor.execute("""INSERT INTO person (name) VALUES (?)""",(full_name,))

def new_transaction(cursor, bank_id, full_name, details,
                    payment_method, t_type, quantity, unit_price):
    cursor.execute("""INSERT INTO transaction_details VALUES(NULL,?,?,?,?,?,?,?);""",
        (bank_id, full_name, details,payment_method, t_type, quantity, unit_price))
