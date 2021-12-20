CREATE TABLE IF NOT EXISTS transactions(id INTEGER PRIMARY KEY,
                            account_id INTEGER,
                            person_name TEXT, 
                            details text,
                            quantity INTEGER,
                            price MONEY,
                            total MONEY ALWAYS AS (quantity * price) STORED,
                            d_date date,
                            d_time time,
                            balance MONEY DEFAULT NULL,
                            FOREIGN KEY (account_id) REFERENCES bank(id)
                                ON DELETE SET NULL);

CREATE TABLE IF NOT EXISTS transaction_type(id INTEGER PRIMARY KEY,
                            transaction_type TEXT,
                            FOREIGN KEY (id) REFERENCES transactions(id)
                                ON DELETE SET NULL);)

CREATE TABLE IF NOT EXISTS bank(
                                    id INTEGER PRIMARY KEY,
                                    name TEXT, 
                                    balance REAL))

CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY,name TEXT))
                              
CREATE TABLE IF NOT EXISTS ownership(
                         id INTEGER PRIMARY KEY,
                         person_id INTEGER, 
                         account_id INTEGER,
                         FOREIGN KEY (person_id) 
                             REFERENCES person(id)
                                 ON DELETE SET NULL,
                         FOREIGN KEY (account_id) 
                             REFERENCES bank(id)
                                 ON DELETE SET NULL)
                                         
CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY,
                        person_id INTEGER,
                        account_id INTEGER,
                        company TEXT,
                        benefits TEXT,
                        type TEXT,
                        FOREIGN KEY(account_id) 
                            REFERENCES bank(id)
                                ON DELETE SET NULL,
                        FOREIGN KEY (person_id) 
                            REFERENCES person(id)
                                ON DELETE SET NULL)
                                


