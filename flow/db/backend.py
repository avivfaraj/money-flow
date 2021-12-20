import sqlite3
from datetime import datetime
import re
from sql.create import create_tables
from sql.insert import insert_person
from sql.trigger import triggers

def date_time():
    time = datetime.now()
    return time.strftime("%H:%M:%S"),time.strftime("%Y/%m/%d")

class CashFlowDB:

    def __init__(self,db):

        # Ensure db was received
        if db:

            # Establish connection
            self.conn = sqlite3.connect(db,timeout=10)

            # Create cursor
            self.cur = self.conn.cursor()

            # Create tables in db
            create_tables(self.cur)
            triggers(self.cur)

            # Commit changes
            self.conn.commit()

        # Error - missing info
        else:
            raise ValueError("Path to a new database or an existing one is missing!")

    def insert_person(self , full_name = "" ):

        # Ensure all parameters received
        if full_name:
            if re.match("([A-Za-z\']{2,}[\s]?){2,3}", full_name):

                insert_person(self.cur, full_name)

                self.conn.commit()

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

    def __del__(self):
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    test = CashFlowDB("./test2.db")
    test.insert_person("Aviv Farag")
    test.delete_person(3)