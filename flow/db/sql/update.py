from sql.insert import execute_query

def update_transaction_dt(conn,t_date, t_time, id_):

    execute_query(conn = conn,
                  query = """UPDATE trans_history
                    SET trans_date = ?,
                    trans_time = ?
                    WHERE transID = ?;""",
                  params = (t_date, t_time, id_))

def update_transaction_qp(conn,quantity, price, id_):

    execute_query(conn = conn,
                  query = """UPDATE trans_details
                    SET quantity = ?,
                    price = ?
                    WHERE transID = ?;""",
                  params = (quantity, price, id_))


