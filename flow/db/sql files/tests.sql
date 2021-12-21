-- Testing

DROP TABLE bank;
DROP TABLE transactions;
DROP TABLE person;
DROP TABLE card;

INSERT INTO bank(id, name, balance) VALUES (123, "Schwab", 10000);
INSERT INTO bank(id, name, balance) VALUES (223, "Schwab", 3333);

INSERT INTO person(name) VALUES ("Rachel");
INSERT INTO card(person_id, account_id, company, benefits, type) VALUES (1,123, "VISA", "nothing", "Debit" );
INSERT INTO card(person_id, account_id, company, benefits, type) VALUES (2,223, "Mastercard", "nothing", "Credit" );


INSERT INTO ownership(person_id, account_id) VALUES (1, 123);
INSERT INTO ownership(person_id, account_id) VALUES (2, 123);
INSERT INTO ownership(person_id, account_id) VALUES (2, 223);


SELECT * FROM person;

SELECT p.name, c.company, c.type 
FROM person as p
JOIN card as c ON p.id = c.person_id;


SELECT p.name, b.name, b.balance 
FROM person as p
JOIN ownership as o ON p.id = o.person_id
JOIN bank as b ON o.account_id = b.id;


INSERT INTO transactions VALUES(NULL,123,"Aviv", "test","Credit","Withdrawal", 2,20,NULL,'14-07-2017','8:44');
INSERT INTO transactions VALUES(NULL,123,"Aviv", "test","Credit","Deposit", 1,58.8,NULL,'14-07-2017','8:44');