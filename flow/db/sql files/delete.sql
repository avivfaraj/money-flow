SELECT * FROM transaction_details;

DELETE FROM transaction_details WHERE ID = 3;

INSERT INTO _Variables (diff) VALUES (CASE
                      WHEN (SELECT total FROM transaction_history WHERE trans_id = 3) > 0
                      THEN -2
                      ELSE 1
                    END);