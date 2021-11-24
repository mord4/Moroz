import datetime
import sqlite3
import time
import telebot
import win10toast

bot = telebot.TeleBot("2125121945:AAGv0F0H9M1wjhej6fvE_y_20EsIcn9e9J0")


def mess(id_chat, text):
    bot.send_message(id_chat, text)


def photo(id_chat, f):
    bot.send_photo(id_chat, photo=open(f, 'rb'))


def date_check():
    d_and_t = str(datetime.datetime.today()).split()
    d = tuple(map(int, d_and_t[0].split("-")))
    a = []
    for table in ("tg_message", "push_notif"):
        f = "notifications.db"
        conn = sqlite3.connect(f)
        query = f"SELECT * FROM {table} WHERE date <= '{d}'"
        r = conn.cursor().execute(query).fetchall()
        query = f"DELETE FROM {table} WHERE date <= '{d}'"
        conn.execute(query)
        a.append(r)
        conn.commit()
        conn.close()
    return a


def pushing(title, text):
    toaster = win10toast.ToastNotifier()
    toaster.show_toast(title, text, duration=3600)


def time_check():
    d_and_t = str(datetime.datetime.today()).split()
    d = tuple(map(int, d_and_t[0].split("-")))
    t = tuple(map(int, d_and_t[1].split(":")[:2]))
    using = []
    for i in res1:
        t_db = tuple(map(int, i[1].split(":")[:2]))
        if t == t_db or d > i[0]:
            message = i[2]
            id_chat = i[3]
            file = i[4]
            mess(id_chat, message)
            if len(file) > 0:
                photo(id_chat, file)
            using.append(i)
    for i in using:
        while i in res1:
            res1.remove(i)
    using = []
    for i in res2:
        t_db = tuple(map(int, i[1].split(":")[:2]))
        if t >= t_db or d > i[0]:
            title = i[2]
            text = i[3]
            pushing(title, text)
            using.append(i)
    for i in using:
        while i in res2:
            res2.remove(i)


while True:
    res = date_check()
    res1 = res[0]
    res2 = res[1]
    print(res1)
    print(res2)
    while len(res1) > 0 or len(res2) > 0:
        time_check()
        time.sleep(20)
    time.sleep(10)
