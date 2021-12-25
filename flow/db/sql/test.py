from sql.insert import *

def automatic_test(conn):
    new_person(conn, "Rachel")
    new_person(conn, "Aviv Farag")

    new_bank(conn, 123,"Schwab", 10000)
    new_bank(conn, 223, "Schwab", 3333)

    new_account_ownership(conn, 1,123)
    new_account_ownership(conn, 2,123)
    new_account_ownership(conn, 2,223)

    new_card(conn, 1,123,"VISA", "Nothing", "Debit")
    new_card(conn, 2,223,"Mastercard", "Nothing", "Credit")


