-- 1
/*UPDATE transaction_history
SET d_date = ?,d_time = ?
WHERE trans_id = ?*/

--2
UPDATE transaction_details
SET quantity = 1, price = 50
WHERE id = 1;

SELECT
CASE WHEN account_id > 123 THEN
CASE WHEN account_id > 223 THEN 4 ELSE 2 END
ELSE 0
END as test
FROM transaction_details;