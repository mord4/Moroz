import telebot
import win10toast


def mess(id_chat, title, text, photo, bot=telebot.TeleBot("2125121945:AAGv0F0H9M1wjhej6fvE_y_20EsIcn9e9J0")):
    bot.send_message(id_chat, title + "\n" * 2 + text)
    if photo != "no":
        bot.send_photo(id_chat, photo=open(photo, 'rb'))


def push(title, text):
    toaster = win10toast.ToastNotifier()
    toaster.show_toast(title=title, msg=text, duration=10)
