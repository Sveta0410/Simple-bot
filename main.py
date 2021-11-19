import telebot
from telebot import types

token = ":)"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я смогу ответить на любой твой вопрос')
    bot.send_message(message.chat.id, 'А ещё ты можешь прислать мне какую-нибудь классную картинку')

@bot.message_handler(content_types=['photo'])
def photo_r(message):
    bot.send_photo(message.chat.id, open('/home/sveta/PycharmProjects/Simple-bot/picture.jpg', 'rb'))

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif '?' in message.text.lower():
        bot.send_message(message.chat.id, 'Гугли.')


if __name__ == '__main__':
    bot.infinity_polling()