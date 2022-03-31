--1
CREATE TRIGGER delete_transaction
BEFORE DELETE
ON trans_details
WHEN OLD.type = "Withdrawal"
BEGIN
    INSERT INTO _Variables VALUES (
                               (OLD.quantity * OLD.price),
                               (SELECT accountID FROM Payment p WHERE p.paymentID = OLD.paymentID));
    
    UPDATE trans_history
    SET balance = balance + (SELECT total FROM _Variables)
    WHERE transID IN 
        (SELECT transID FROM trans_details WHERE paymentID IN 
        (SELECT paymentID FROM Payment WHERE accountID = (SELECT bankID FROM _Variables)))
    AND
        transID > OLD.transID;
    
    UPDATE bank
    SET balance = balance + (SELECT total FROM _Variables)
    WHERE accountID = (SELECT bankID FROM _Variables);
    
    DELETE FROM _Variables;
END;


--2
CREATE TRIGGER update_withdrawal
AFTER UPDATE
ON trans_details
WHEN OLD.type = "Withdrawal"
BEGIN
    INSERT INTO _Variables VALUES (
                               (CASE WHEN (NEW.quantity * NEW.price > OLD.quantity * OLD.price) 
                                THEN - (NEW.quantity * NEW.price - OLD.quantity * OLD.price) 
                                ELSE (OLD.quantity * OLD.price - NEW.quantity * NEW.price) 
                                END),
                               (SELECT accountID FROM Payment p WHERE p.paymentID = OLD.paymentID));

    UPDATE trans_history
    SET balance = balance + (SELECT total FROM _Variables),
        total = - (NEW.quantity * NEW.price) 
    WHERE transID = OLD.transID;
    
    UPDATE trans_history
    SET balance = balance + (SELECT total FROM _Variables)
    WHERE transID IN (
               SELECT transID FROM trans_details
               WHERE paymentID IN (
                          SELECT paymentID
                          FROM Payment p
                          WHERE p.accountID = (SELECT bankID FROM _Variables)
                          )
                     )
    AND 
        transID > OLD.transID;
    
    UPDATE bank
    SET balance = balance + (SELECT total FROM _Variables)
    WHERE accountID = (SELECT bankID FROM _Variables);
    
    DELETE FROM _Variables;
END;


--3
CREATE TRIGGER update_deposit
AFTER UPDATE
ON trans_details
WHEN OLD.type = "Deposit"
BEGIN
    INSERT INTO _Variables VALUES (
                               (CASE WHEN (NEW.quantity * NEW.price > OLD.quantity * OLD.price)
                                THEN (NEW.quantity * NEW.price - OLD.quantity * OLD.price)
                                ELSE -(OLD.quantity * OLD.price - NEW.quantity * NEW.price)
                                END),
                               (SELECT accountID FROM Payment p WHERE p.paymentID = OLD.paymentID));

    UPDATE trans_history
    SET balance = balance + (SELECT total FROM _Variables),
        total = (NEW.quantity * NEW.price) 
    WHERE transID = OLD.transID;
    
    UPDATE trans_history
    SET balance = balance + (SELECT total FROM _Variables)
    WHERE transID IN (
               SELECT transID FROM trans_details
               WHERE paymentID IN (
                          SELECT paymentID
                          FROM Payment p
                          WHERE p.accountID = (SELECT bankID FROM _Variables)
                          )
                     )
    AND 
        transID > OLD.transID;
    
    UPDATE bank
    SET balance = balance + (SELECT total FROM _Variables)
    WHERE accountID = (SELECT bankID FROM _Variables);
    
    DELETE FROM _Variables;
END;


--4
CREATE TRIGGER new_withdrawal
AFTER INSERT 
ON trans_details
WHEN new.type = 'Withdrawal'
BEGIN
    INSERT INTO _Variables VALUES (
                               (NEW.quantity * NEW.price - NEW.discount),
                               (SELECT accountID FROM Payment WHERE paymentID = NEW.paymentID));
    
    UPDATE Bank
    SET balance = balance - (SELECT total FROM _Variables)
    WHERE Bank.accountID = (SELECT bankID FROM _Variables);

    INSERT INTO trans_history (transID, total,balance)
    VALUES (NEW.transID,
            -(SELECT total FROM _Variables),
            (SELECT balance 
             FROM Bank 
             WHERE Bank.accountID = (SELECT bankID FROM _Variables)
             ));

    DELETE FROM _Variables;
END;


--5
CREATE TRIGGER new_deposit
AFTER INSERT
ON trans_details
WHEN NEW.type = 'Deposit'
BEGIN
    INSERT INTO _Variables VALUES (
                               (NEW.quantity * NEW.price - NEW.discount),
                               (SELECT accountID FROM Payment 
                                WHERE paymentID = NEW.paymentID));

    UPDATE Bank
    SET balance = balance + (SELECT total FROM _Variables)
    WHERE Bank.accountID = (SELECT bankID FROM _Variables);
    
    INSERT INTO trans_history (transID, total, balance)
    VALUES (NEW.transID,
            (SELECT total FROM _Variables),
            (SELECT balance FROM Bank 
             WHERE bank.accountID = (SELECT bankID FROM _Variables)
             ));

    DELETE FROM _Variables;
END;