import sqlite3

def triggers(cursor):
    if isinstance(cursor, sqlite3.Cursor):
        transaction_trigger(cursor)
    else:
        raise TypeError("Invalid sqlite3 cursor") 

def transaction_trigger(cursor):
    cursor.executescript("""
            CREATE TRIGGER IF NOT EXISTS withdraw 
            AFTER INSERT
            ON transaction_details
            WHEN NEW.type = "Withdrawal"
            BEGIN
             UPDATE bank
             SET balance = balance - (NEW.quantity * NEW.price)
             WHERE id = NEW.account_id;

             INSERT INTO transaction_history (total, balance)
             VALUES (-NEW.quantity * NEW.price, (SELECT balance FROM bank WHERE id = NEW.account_id));
            END;
            
    
            CREATE TRIGGER IF NOT EXISTS deposit 
            AFTER INSERT
            ON transaction_details
            WHEN NEW.type = "Deposit"
            BEGIN
             UPDATE bank
             SET balance = balance + (NEW.quantity * NEW.price)
             WHERE id = NEW.account_id;

             INSERT INTO transaction_history (total, balance)
             VALUES (NEW.quantity * NEW.price, (SELECT balance FROM bank WHERE id = NEW.account_id));
            END;""")


