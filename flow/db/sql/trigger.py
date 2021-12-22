from sql.insert import execute_query

def triggers(conn):
    transaction_trigger(conn)

def transaction_trigger(conn):
    execute_query(conn = conn,
                  query = """CREATE TRIGGER IF NOT EXISTS withdraw 
                            AFTER INSERT
                            ON transaction_details
                            WHEN NEW.type = "Withdrawal"
                            BEGIN
                             UPDATE bank
                             SET balance = balance - (NEW.quantity * NEW.price)
                             WHERE id = NEW.account_id;

                             INSERT INTO transaction_history (total, balance)
                             VALUES (-NEW.quantity * NEW.price, (SELECT balance FROM bank WHERE id = NEW.account_id));
                            END;""",
                  params = ())

    execute_query(conn = conn,
                  query = """
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
                            END;
                            """,
                  params = ())



