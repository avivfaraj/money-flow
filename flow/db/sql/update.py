
def update_transaction(cursor,t_date, t_time, id_):
    cursor.execute("""UPDATE transaction_history
                    SET d_date = ?,
                    d_time = ?
                    WHERE trans_id = ?""",
        (t_date, t_time, id_))
