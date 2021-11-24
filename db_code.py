import sqlite3


fileName = "notifications.db"
connection = sqlite3.connect(fileName)
query = """
    select * from tg_message
"""
res = connection.cursor().execute(query).fetchall()
for row in res:
    print(row)
print()
query = """
    select * from push_notif
"""
res = connection.cursor().execute(query).fetchall()
for row in res:
    print(row)

connection.close()
