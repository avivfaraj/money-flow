from sql.insert import *

def automatic_test(conn):

    new_person(conn, "Hila", "Hadar")
    new_person(conn, "Hadas","Filsberg", "Roy")

    new_bank(conn, 123,"Schwab", 10000)
    new_bank(conn, 223, "Schwab", 3333)

    new_account_ownership(conn, 1,123)
    new_account_ownership(conn, 2,123)
    new_account_ownership(conn, 2,223)

    new_card(conn, 4144,123,"Visa", "Debit", 2)
    new_card(conn, 2222,223,"Mastercard", "Credit", 1)


