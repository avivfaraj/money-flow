from sql.insert import execute_query

def update_transaction(conn,t_date, t_time, id_):

    execute_query(conn = conn,
                  query = """UPDATE transaction_history
                    SET d_date = ?,
                    d_time = ?
                    WHERE trans_id = ?;""",
                  params = (t_date, t_time, id_))


