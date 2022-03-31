import sqlite3
from datetime import datetime
import re
from sql.create import create_tables
from sql.insert import new_person, new_transaction, execute_query, new_bank
from sql.trigger import triggers
from sql.update import update_transaction_dt,update_transaction_qp
from sql.test import automatic_test as tst


def date_time(time = datetime.now()):

    return time.strftime("%H:%M"),time.strftime("%Y-%m-%d")

class CashFlowDB:

    def __init__(self,db: str) -> None:

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
        tst(self.conn)

    def insert_person(self, 
                      first_name: str = "", 
                      middle_name: str = "", 
                      last_name: str = "" ):

        # Ensure all parameters received
        if first_name and last_name:

            new_person(self.conn, first_name, middle_name, last_name)

        else:
            raise ValueError("Name is invalid")

    def delete_person(self, ID: int = None):
        if ID:
            try:  
                self.cur.execute("DELETE FROM person WHERE id = ?",
                            (ID,))

                self.conn.commit()
                # print(self.cur.rowcount) # Number of rows deleted
            except sqlite3.OperationalError as err:
                print("** Error **", err)

        # Error - missing info
        else:
            raise ValueError("Name is missing!")


    def insert_transaction(self,
                           details: str,
                           sector: str, 
                           t_type: str,
                           quantity: int, 
                           unit_price: float, 
                           discount: float, 
                           payment_id: int,
                           timestamp: datetime = datetime.now()):

        # Insert new transaction
        last_id = new_transaction(self.conn,details,sector,
                     t_type, quantity, unit_price, discount, payment_id)

        # Time and date
        t,d = date_time(timestamp)

        # Update transaction's time and date in transaction_history
        update_transaction_dt(self.conn, d,t, last_id)

    def update_transaction(self, trans_id, quantity, price):
        update_transaction_qp(self.conn, quantity, price, trans_id)

    def new_account(self, account_id, account_name, balance = 0):
        new_bank(self.conn, account_id, account_name, balance)
        
    def __del__(self):
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    test = CashFlowDB("./test3.db")

    # Tests
    test.run_test()
    test.insert_transaction("test","Fashion","Withdrawal", 1, 100, 0, 2222)
    test.insert_transaction("Another Test","Salary","Deposit", 1, 200, 0, 10001)

# List of errors: 
# 1) FOREIGN KEY constraint failed - sqlite3.IntegrityError
#    Since this error does not include the field in which the error occured,
#    the best way to deal with it is to check if FOREIGN KEYS exist in database.
