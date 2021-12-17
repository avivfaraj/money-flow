CREATE TABLE IF NOT EXISTS transactions(id INTEGER PRIMARY KEY, bank_account INTEGER, details TEXT, amount INTEGER, unit_price REAL,total REAL, t_date date, t_time time);
CREATE TABLE IF NOT EXISTS bank(id INTEGER PRIMARY KEY UNIQUE, name TEXT, balance REAL);
CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY,
                                  name TEXT);
                              
CREATE TABLE IF NOT EXISTS ownership(id INTEGER PRIMARY KEY,
                                     person_id INTEGER, 
                                     account_id INTEGER,
                                     FOREIGN KEY (person_id) REFERENCES person(id)
                                         ON DELETE SET NULL,
                                     FOREIGN KEY (account_id) REFERENCES bank(id)
                                         ON DELETE SET NULL);
                                         
CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY,
                                person_id INTEGER,
                                account_id INTEGER,
                                company TEXT,
                                benefits TEXT,
                                type TEXT,
                                FOREIGN KEY(account_id) REFERENCES bank(id)
                                ON DELETE SET NULL,
                                FOREIGN KEY (person_id) REFERENCES person(id)
                                ON DELETE SET NULL);
                                

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