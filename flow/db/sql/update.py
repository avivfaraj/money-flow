from sql.insert import execute_query

def update_transaction_dt(conn,t_date, t_time, id_):

    execute_query(conn = conn,
                  query = """UPDATE transaction_history
                    SET d_date = ?,
                    d_time = ?
                    WHERE trans_id = ?;""",
                  params = (t_date, t_time, id_))

def update_transaction_qp(conn,quantity, price, id_):

    execute_query(conn = conn,
                  query = """UPDATE transaction_details
                    SET quantity = ?,
                    price = ?
                    WHERE id = ?;""",
                  params = (quantity, price, id_))


