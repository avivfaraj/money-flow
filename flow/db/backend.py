import sqlite3
from datetime import datetime
import re
from sql.create import create_tables
from sql.insert import insert_person, new_transaction
from sql.trigger import triggers
from sql.update import update_transaction
from sql.test import test as tst

def date_time():
    time = datetime.now()
    return time.strftime("%H:%M"),time.strftime("%Y-%m-%d")

class CashFlowDB:

    def __init__(self,db):

        # Ensure db was received
        if db:

            # Establish connection
            self.conn = sqlite3.connect(db,timeout=10)

            # Create cursor
            self.cur = self.conn.cursor()

            # Create tables in db
            create_tables(self.conn)
            triggers(self.conn)

        # Error - missing info
        else:
            raise ValueError("Path to a new database or an existing one is missing!")

    def run_test(self):
        tst(self.cur)

    def insert_person(self , full_name = "" ):

        # Ensure all parameters received
        if full_name:
            if re.match("([A-Za-z\']{2,}[\s]?){2,3}", full_name):

                insert_person(self.conn, full_name)

            else:
                raise ValueError("Name is not valid!")

        # Missing info
        else:
            raise ValueError("Name is missing!")

    def delete_person(self, ID = None):
        if ID:  
            self.cur.execute("DELETE FROM person WHERE id = ?",
                            (ID,))

            self.conn.commit()
            print(self.cur.rowcount) # Number of rows deleted

        # Error - missing info
        else:
            raise ValueError("Name is missing!")


    def insert_transaction(self,bank_id, full_name, details,
                    payment_method, t_type, quantity, unit_price):

        # Insert new transaction
        last_id = new_transaction(self.conn,bank_id, full_name, details,
                    payment_method, t_type, quantity, unit_price)

        # Time and date
        t,d = date_time()

        # Update transaction's time and date in transaction_history
        update_transaction(self.conn, d,t, last_id)


    def __del__(self):
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    test = CashFlowDB("./test2.db")
    # test.insert_person("Rachel Farag")
    # test.delete_person(3)

    # Tests
    # test.run_test()
    test.insert_transaction(123,"Aviv", "test","Credit","Withdrawal", 1, 380)
    # test.insert_transaction(123,"Aviv", "test","Credit","Deposit", 2, 10.5)

