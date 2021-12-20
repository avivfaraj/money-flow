CREATE TRIGGER IF NOT EXISTS update_balance 
            AFTER INSERT
            ON transactions
            BEGIN
             UPDATE bank
             SET balance = balance - NEW.total
             WHERE id = NEW.account_id;
            END;
                                         
CREATE TRIGGER IF NOT EXISTS update_transaction_balance
            AFTER UPDATE OF balance
            ON bank
            BEGIN
                 UPDATE transactions
                 SET balance = NEW.balance
                 WHERE account_id = NEW.id AND id = (SELECT MAX(id) FROM transactions);
            END;
                                         