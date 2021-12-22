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
     END;

                   
CREATE TRIGGER IF NOT EXISTS update_transaction_balance
AFTER UPDATE OF balance
ON bank
     BEGIN
          UPDATE transactions
          SET balance = NEW.balance
          WHERE account_id = NEW.id AND id = (SELECT MAX(id) FROM transactions);
     END;
                                         