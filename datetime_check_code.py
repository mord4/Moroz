from db_code import get_data, delete_data
import datetime
import time
import telebot
import win10toast


def mess(id_chat, text, bot=telebot.TeleBot("2125121945:AAGv0F0H9M1wjhej6fvE_y_20EsIcn9e9J0")):
    bot.send_message(id_chat, text)


def photo(id_chat, f, bot=telebot.TeleBot("2125121945:AAGv0F0H9M1wjhej6fvE_y_20EsIcn9e9J0")):
    bot.send_photo(id_chat, photo=open(f, 'rb'))


def date_check():
    d_and_t = str(datetime.datetime.today()).split()
    d = tuple(map(int, d_and_t[0].split("-")))
    a = []
    for table in ("tg_message", "push_notif"):
        r = get_data(table, d)
        a.append(r)
    return a


def pushing(title, text):
    toaster = win10toast.ToastNotifier()
    toaster.show_toast(title=title, msg=text)


def time_check():
    d_and_t = str(datetime.datetime.today()).split()
    d = tuple(map(int, d_and_t[0].split("-")))
    t = tuple(map(int, d_and_t[1].split(":")[:2]))
    using1 = []
    for i in res1:
        t_db = tuple(map(int, i[1].split(":")[:2]))
        d_db = tuple(map(int, i[0][1:-1].split(", ")))
        if t >= t_db or d > d_db:
            message = str(i[2])
            id_chat = i[3]
            file = i[4]
            if len(str(id_chat)) != 10:
                print("++++")
                print("ID не заполнен.\n", i, "\nДанное сообщение не может быть отправлено.")
                print("++++")
                delete_data("tg_message", i)
            else:
                mess(id_chat, message)
                if not(file is None):
                    photo(id_chat, file)
            delete_data("tg_message", i)
            using1.append(i)
    using2 = []
    for i in res2:
        t_db = tuple(map(int, i[1].split(":")[:2]))
        d_db = tuple(map(int, i[0][1:-1].split(", ")))
        if t >= t_db or d > d_db:
            title = str(i[2])
            text = str(i[3])
            pushing(title, text)
            delete_data("push_notif", i)
            using2.append(i)
    for i in using1:
        while i in res1:
            res1.remove(i)
    for i in using2:
        while i in res2:
            res2.remove(i)


try:
    while True:
        res = date_check()
        res1 = res[0]
        res2 = res[1]
        print(res1)
        print(res2)
        time_check()
        time.sleep(5)
except():
    print("Ошибка, проверьте входные данные и работоспособность кода.")
