def test(cursor):
    cursor.executescript("""INSERT INTO bank(id, name, balance) VALUES (123, "Schwab", 10000);
INSERT INTO bank(id, name, balance) VALUES (223, "Schwab", 3333);

INSERT INTO person(name) VALUES ("Rachel");
INSERT INTO person(name) VALUES ("Aviv Farag");

INSERT INTO card(person_id, account_id, company, benefits, type) VALUES (1,123, "VISA", "nothing", "Debit" );
INSERT INTO card(person_id, account_id, company, benefits, type) VALUES (2,223, "Mastercard", "nothing", "Credit" );


INSERT INTO ownership(person_id, account_id) VALUES (1, 123);
INSERT INTO ownership(person_id, account_id) VALUES (2, 123);
INSERT INTO ownership(person_id, account_id) VALUES (2, 223);""")