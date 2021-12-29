DROP TRIGGER delete_transaction;
CREATE TRIGGER delete_transaction
BEFORE DELETE
ON transaction_details
BEGIN
INSERT INTO _Variables (diff) VALUES (CASE
                      WHEN OLD.type = "Deposit"
                      THEN -(OLD.quantity * OLD.price)
                      ELSE OLD.quantity * OLD.price
                    END);
                    
UPDATE transaction_history
      SET balance = balance + (SELECT diff FROM _Variables)
      WHERE trans_id IN (SELECT id FROM transaction_details WHERE account_id = OLD.account_id) AND trans_id > OLD.id;
UPDATE bank
      SET balance = balance + (SELECT diff FROM _Variables)
      WHERE id = OLD.account_id;
DELETE FROM _Variables WHERE id =1;
END;


DROP TRIGGER update_transaction;
CREATE TRIGGER update_transaction
AFTER UPDATE
ON transaction_details
BEGIN
INSERT INTO _Variables (diff) VALUES (CASE
                      WHEN OLD.type = "Deposit" THEN 
                          CASE WHEN (NEW.quantity * NEW.price > OLD.quantity * OLD.price)
                               THEN (NEW.quantity * NEW.price - OLD.quantity * OLD.price)
                               ELSE -(OLD.quantity * OLD.price - NEW.quantity * NEW.price)
                          END
                      ELSE
                          CASE WHEN (NEW.quantity * NEW.price > OLD.quantity * OLD.price)
                               THEN -(NEW.quantity * NEW.price - OLD.quantity * OLD.price)
                               ELSE (OLD.quantity * OLD.price - NEW.quantity * NEW.price)
                          END
                      END
                    );
UPDATE transaction_history
      SET 
      balance = balance + (SELECT diff FROM _Variables),
      total = CASE OLD.type 
                        WHEN "Withdrawal" 
                        THEN -(NEW.quantity * NEW.price) 
                        ELSE (NEW.quantity * NEW.price) 
                        END
      WHERE trans_id = OLD.id;
UPDATE transaction_history
      SET balance = balance + (SELECT diff FROM _Variables)
      WHERE trans_id IN (SELECT id FROM transaction_details WHERE account_id = OLD.account_id) AND trans_id > OLD.id;
UPDATE bank
      SET balance = balance + (SELECT diff FROM _Variables)
      WHERE id = OLD.account_id;
DELETE FROM _Variables WHERE id =1;
END;



CREATE TRIGGER insert_transaction
AFTER INSERT
ON transaction_details
BEGIN
INSERT INTO _Variables (diff) VALUES (CASE
                      WHEN NEW.type = "Deposit" 
                      THEN 
                          NEW.quantity * NEW.price
                      ELSE
                          -NEW.quantity * NEW.price
                      END
                    );
UPDATE bank
          SET balance = balance + (SELECT diff FROM _Variables)
          WHERE id = NEW.account_id;
INSERT INTO transaction_history (total, balance)
          VALUES ((SELECT diff FROM _Variables), (SELECT balance FROM bank WHERE id = NEW.account_id));
DELETE FROM _Variables WHERE id =1;
END;