def insert_person(cursor, full_name):
    if cursor:
        cursor.execute("""INSERT INTO person (name) VALUES (?)""",(full_name,))
