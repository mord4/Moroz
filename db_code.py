import sqlite3


def get_data(table, d):
    conn = sqlite3.connect("notifications.db")
    query = f"SELECT * FROM {table} WHERE date <= '{d}'"
    r = conn.cursor().execute(query).fetchall()
    conn.close()
    return r


def delete_data(table, res):
    conn = sqlite3.connect("notifications.db")
    if len(res) == 5:
        query = f"DELETE FROM {table} " \
                f"WHERE date='{res[0]}' and time='{res[1]}' " \
                f"and message='{res[2]}' and chat_id='{res[3]}' " \
                f"and file='{res[4]}'"
    else:
        query = f"DELETE FROM {table} " \
                f"WHERE date='{res[0]}' and time='{res[1]}' " \
                f"and title='{res[2]}' and text='{res[3]}'"
    print(res)
    print(query)
    conn.execute(query)
    conn.commit()

