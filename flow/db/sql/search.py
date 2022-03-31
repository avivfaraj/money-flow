import sqlite3

def select_query(conn: "sqlite3.Connection",
                 query: str, 
                 params: tuple, 
                 fetch_one: bool = False):
    """
    Execute a SELECT query. 

    Input:
    Conn -> connection to sqlite3 database
    query -> String query to be executed
    params -> tuple of parameters for the query
    fetch_one -> False to fetch more than one line.

    Return:
    List of instances from database
    """
    if isinstance(conn,sqlite3.Connection):
        cur = conn.cursor()
        cur.execute(query, params)
        
        if fetch_one:
            return cur.fetchone()

        return cur.fetchall() 

    else:
        raise TypeError("No connection to database") 


if __name__ == "__main__":
    # test
    conn = sqlite3.connect("../test3.db")
    print(select_query(conn, "SELECT * FROM person WHERE id = ?;", (2,), fetch_one = True))
    print([id_[0] for id_ in select_query(conn,
                           "SELECT id FROM bank;",())])