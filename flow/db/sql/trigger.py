from sql.insert import execute_query

def triggers(conn):
	# delete_transaction_trigger(conn)
	# update_transaction_trigger(conn)
	insert_transaction_trigger(conn)
	
# def delete_transaction_trigger(conn):
# 	execute_query(conn = conn,
# 				  query = """CREATE TRIGGER IF NOT EXISTS delete_transaction
# 							 BEFORE DELETE
# 							 ON transaction_details
# 							 BEGIN
# 							 	INSERT INTO _Variables (diff) VALUES (CASE
# 							                      WHEN OLD.type = "Deposit"
# 							                      THEN -(OLD.quantity * OLD.price)
# 							                      ELSE OLD.quantity * OLD.price
# 							                    END);
							                    
# 								UPDATE transaction_history
# 							      	SET balance = balance + (SELECT diff FROM _Variables)
# 							      	WHERE trans_id IN (SELECT id FROM transaction_details WHERE account_id = OLD.account_id) AND trans_id > OLD.id;

# 								UPDATE bank
# 							      	SET balance = balance + (SELECT diff FROM _Variables)
# 							      	WHERE id = OLD.account_id;

# 								DELETE FROM _Variables WHERE id =1;
# 							 END;
# 							""")


# def update_transaction_trigger(conn):

# 	execute_query(conn = conn,
# 				  query = """
# 							CREATE TRIGGER IF NOT EXISTS update_transaction
# 							AFTER UPDATE
# 							ON transaction_details
# 							BEGIN
# 								INSERT INTO _Variables (diff) VALUES (CASE
# 								                      WHEN OLD.type = "Deposit" THEN 
# 								                          CASE WHEN (NEW.quantity * NEW.price > OLD.quantity * OLD.price)
# 								                               THEN (NEW.quantity * NEW.price - OLD.quantity * OLD.price)
# 								                               ELSE -(OLD.quantity * OLD.price - NEW.quantity * NEW.price)
# 								                          END
# 								                      ELSE
# 								                          CASE WHEN (NEW.quantity * NEW.price > OLD.quantity * OLD.price)
# 								                               THEN -(NEW.quantity * NEW.price - OLD.quantity * OLD.price)
# 								                               ELSE (OLD.quantity * OLD.price - NEW.quantity * NEW.price)
# 								                          END
# 								                      END);

# 								UPDATE transaction_history
# 								      SET 
# 								      balance = balance + (SELECT diff FROM _Variables),
# 								      total = CASE OLD.type 
# 								                        WHEN "Withdrawal" 
# 								                        THEN -(NEW.quantity * NEW.price) 
# 								                        ELSE (NEW.quantity * NEW.price) 
# 								                        END
# 								      WHERE trans_id = OLD.id;

# 								UPDATE transaction_history
# 								      SET balance = balance + (SELECT diff FROM _Variables)
# 								      WHERE trans_id IN (SELECT id FROM transaction_details WHERE account_id = OLD.account_id) AND trans_id > OLD.id;

# 								UPDATE bank
# 								      SET balance = balance + (SELECT diff FROM _Variables)
# 								      WHERE id = OLD.account_id;

# 								DELETE FROM _Variables WHERE id =1;
# 							END;
# 							""")


def insert_transaction_trigger(conn):

	execute_query(conn = conn,
				  query = """
							CREATE TRIGGER new_withdrawal
         AFTER INSERT
            ON trans_details
          WHEN new.type = 'Withdrawal'
BEGIN
    INSERT INTO _Variables VALUES (
                               (NEW.quantity * NEW.price - NEW.discount),
                               (
                                   SELECT accountID
                                     FROM Payment
                                    WHERE paymentID = NEW.paymentID
                               )
                           );
    UPDATE Bank
       SET balance = balance - (
                                   SELECT total
                                     FROM _Variables
                               )
     WHERE Bank.accountID = (
                                SELECT bankID
                                  FROM _Variables
                            );
    INSERT INTO trans_history (
                                transID,
                                total,
                                balance
                              )
                              VALUES (
                                  NEW.transID,
-                                 (
                                      SELECT total
                                        FROM _Variables
                                  ),
                                  (
                                      SELECT balance
                                        FROM Bank
                                       WHERE bank.accountID = (
                                                                  SELECT bankID
                                                                    FROM _Variables
                                                              )
                                  )
                              );
    DELETE FROM _Variables;
END;
							""")

	execute_query(conn = conn,
				  query = """
CREATE TRIGGER new_deposit
         AFTER INSERT
            ON trans_details
          WHEN NEW.type = 'Deposit'
BEGIN
    INSERT INTO _Variables VALUES (
                               (NEW.quantity * NEW.price - NEW.discount),
                               (
                                   SELECT accountID
                                     FROM Payment
                                    WHERE paymentID = NEW.paymentID
                               )
                           );
    UPDATE Bank
       SET balance = balance + (
                                   SELECT total
                                     FROM _Variables
                               )
     WHERE Bank.accountID = (
                                SELECT bankID
                                  FROM _Variables
                            );
    INSERT INTO trans_history (
                                  transID,
                                  total,
                                  balance
                              )
                              VALUES (
                                  NEW.transID,
                                  (
                                      SELECT total
                                        FROM _Variables
                                  ),
                                  (
                                      SELECT balance
                                        FROM Bank
                                       WHERE bank.accountID = (
                                                                  SELECT bankID
                                                                    FROM _Variables
                                                              )
                                  )
                              );
    DELETE FROM _Variables;
END;""")






