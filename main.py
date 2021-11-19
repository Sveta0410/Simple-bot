import telebot
import random
from telebot import types

token = ":)"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('Привет!', "/help")
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я постараюсь поднять тебе настроение\n' +
                     'И помогу найти ответ на любой вопрос :) \n' +
                     '\n' +
                     'Список команд:\n' +
                     '/meme - бот отправит забавную картиночку\n' +
                     '/cat - бот отправит милого котика\n' +
                     '/watch - бот отправит ссылку на добрый мультик')

@bot.message_handler(commands=['meme'])
def get_picture(message):
    x = str(random.randint(1, 6))
    way = '/home/sveta/PycharmProjects/Simple-bot/pictures/' + x + '.jpg'
    bot.send_photo(message.chat.id, open(way, 'rb'))

@bot.message_handler(commands=['cat'])
def get_picture(message):
    x = str(random.randint(1, 5))
    way = '/home/sveta/PycharmProjects/Simple-bot/cat_pictures/' + x + '.jpg'
    bot.send_photo(message.chat.id, open(way, 'rb'))

@bot.message_handler(commands=['watch'])
def get_cartoon(message):
    x = random.randint(1, 3)
    if x == 1:
        link = 'https://www.youtube.com/watch?v=-W2tJmIJltg&list=PLF6D0792910A41A09'
    elif x == 2:
        link = 'https://www.youtube.com/watch?v=mkeHiEhnNW4'
    elif x == 3:
        link = 'https://www.youtube.com/watch?v=yLVOrQjeMPc'

    bot.send_message(message.chat.id, link)

@bot.message_handler(content_types=['photo'])
def photo_r(message):
    bot.send_photo(message.chat.id, open('/home/sveta/PycharmProjects/Simple-bot/pictures/picture.jpg', 'rb'))

@bot.message_handler(content_types=['text'])
def answer(message):
    if '?' in message.text.lower():
        bot.send_message(message.chat.id, 'Гугли - https://www.google.com')
        bot.send_message(message.chat.id, ':)')
    elif message.text.lower() == "ясно":
        bot.send_message(message.chat.id, 'Понятно')
    elif "спасибо" in message.text.lower():
        bot.send_message(message.chat.id, 'Не благодари)')
    elif "привет" in message.text.lower():
        keyboard = types.InlineKeyboardMarkup()
        key_how1 = types.InlineKeyboardButton(text='Отлично!', callback_data='great')
        keyboard.add(key_how1)
        key_how2 = types.InlineKeyboardButton(text='Неплохо', callback_data='so so')
        keyboard.add(key_how2)
        key_how3 = types.InlineKeyboardButton(text='Так себе :(', callback_data=':(')
        keyboard.add(key_how3)
        bot.send_message(message.chat.id, 'Как дела?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'great':
        bot.send_message(call.message.chat.id, 'Я очень рад за тебя!')
        bot.send_message(call.message.chat.id, 'Чтобы поддержать прекрасное настроение, предлагаю посмотреть на' +
                                               ' забавные картинки /meme или на милых котиков /cat\n'
                                               'А если у тебя есть немного времени, советую посмотреть ' +
                                               'какой-нибудь мультик /watch')
    elif call.data == 'so so':
        bot.send_message(call.message.chat.id, '...предлагаю попробовать улучшить настроение)')
        bot.send_message(call.message.chat.id, 'Думаю, забавные картинки /meme или котики /cat могут помочь\n'
                                               'А если у тебя есть немного времени, советую посмотреть ' +
                                               'какой-нибудь мультик /watch')
    elif call.data == ':(':
        bot.send_message(call.message.chat.id, 'С этим срочно нужно что-то делать!!!\n'
                                               'Хочешь, я отправлю тебе милого котика?... /cat\n'
                                               'Или мне стоит попробовать развеселить тебя забавной картинкой? /meme\n'
                                               'А если у тебя есть немного времени, советую посмотреть ' +
                                               'какой-нибудь мультик /watch')
        bot.send_message(call.message.chat.id, 'А может у тебя какие-то проблемы с учёбой?\n' +
                                               'Можешь задать мне любой вопрос, я помогу')


if __name__ == '__main__':
    bot.infinity_polling()