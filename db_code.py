import sqlite3


def get_data(date=None):
    conn = sqlite3.connect("moroz_db.db")
    if date is not None:
        query = f"SELECT * FROM Noty WHERE date <= '{date}'"
    else:
        query = f"SELECT * FROM Noty"
    r = conn.cursor().execute(query).fetchall()
    conn.close()
    return r


def add_data(*values):
    date, time, title, text, tg, push, email, photo = values
    conn = sqlite3.connect("moroz_db.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO Noty (date, time, title, text, telegram, push, email, photo) "
                   f"VALUES ('{date}', '{time}', '{title}', '{text}', '{tg}', '{push}', '{email}', '{photo}')")
    conn.commit()


def get_id(tg_id):
    conn = sqlite3.connect("moroz_db.db")
    cursor = conn.cursor()
    info = cursor.execute(f"SELECT * FROM tgid WHERE id='{tg_id}'")
    if info.fetchone() is None:
        conn.close()
        return True
    conn.close()
    return False


def add_id(tg_id):
    conn = sqlite3.connect("moroz_db.db")
    cursor = conn.cursor()
    if get_id(tg_id):
        cursor.execute(f"INSERT INTO tgid (id) VALUES ('{tg_id}')")
        conn.commit()


def delete_data(*values):
    date, time, title, text, tg, push, email, photo = values
    conn = sqlite3.connect("moroz_db.db")
    query = f"DELETE FROM Noty" \
            f"WHERE date='{date}' and time='{time}' " \
            f"and title='{title}' and text='{text}' and telegram='{tg}' " \
            f"and push='{push}' and email='{email}' and photo='{photo}'"
    conn.execute(query)
    conn.commit()