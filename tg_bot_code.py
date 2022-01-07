from db_code import add_id
import telebot

bot = telebot.TeleBot("2125121945:AAGv0F0H9M1wjhej6fvE_y_20EsIcn9e9J0")


@bot.message_handler(commands=['start'])
def start(message):
    a = str(message.chat.id)
    bot.send_message(message.chat.id, "Привет, я бот Moroz, я не принимаю сообщения, а только отправляю их.\n"
                                      "\n"
                                      "ID: " + a)
    add_id(a)


@bot.message_handler(content_types=["text", "document", "audio"])
def start(message):
    bot.send_message(message.chat.id, "Вы конечно можете писать сообщения, оставляя заметки, но я не отвечу.")


bot.polling()
