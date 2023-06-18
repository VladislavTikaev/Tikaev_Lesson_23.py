#6018742290:AAGtDaUtU_5LZILS5ePCaeBwRp-kTDalBF8
import telebot
from telebot import types
token = '6018742290:AAGtDaUtU_5LZILS5ePCaeBwRp-kTDalBF8'
bot = telebot.TeleBot(token)

def create_keyboard():
    keyboard = types.InlineKeyboardMarkup() #создает клавиатуру
    anekdot_button = types.InlineKeyboardButton(text= 'Хочу анекдот', callback_data='1') #создает кнопку
    sleep_button = types.InlineKeyboardButton(text='Хочу спать', callback_data='2')
    bye_button = types.InlineKeyboardButton(text='Прощание', callback_data='3')
    hello_button = types.InlineKeyboardButton(text='Приветствие', callback_data='4')
    pogoda_gomel_button = types.InlineKeyboardButton(text='Прогноз погоды г.Гомель', callback_data='5')
    keyboard.add(anekdot_button, sleep_button, bye_button, hello_button, pogoda_gomel_button)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, 'Выберите, что вы хотите: ', reply_markup=create_keyboard())

@bot.callback_query_handler(func=lambda call: True if call.message else False)
def callback_inline(call):
    if call.message:
        if call.data == '1':
            img = 'https://fikiwiki.com/uploads/posts/2022-02/1644999908_8-fikiwiki-com-p-samie-smeshnie-anekdoti-s-kartinkami-9.jpg'
            bot.send_photo(call.message.chat.id, photo=img, caption='Смешной анекдот', reply_markup=create_keyboard())
        if call.data == '2':
            audio = open("sleep.mp3", 'rb')
            bot.send_audio(call.message.chat.id, audio=audio, caption='Засыпай:)', reply_markup=create_keyboard())
        if call.data == '3':
            img = 'http://kartinkived.ru/wp-content/uploads/2021/05/48-7.jpg'
            bot.send_photo(call.message.chat.id, photo=img, reply_markup=create_keyboard())
        if call.data == '4':
            img = 'https://i.pinimg.com/originals/41/74/ea/4174ea1fba5a3f03e6b12a03b4ef759a.jpg'
            bot.send_photo(call.message.chat.id, photo=img, reply_markup=create_keyboard())
        if call.data == '5':
            img = 'https://rusmeteo.net/socialimg/gomel/monthly/'
            bot.send_photo(call.message.chat.id, photo=img, reply_markup=create_keyboard())
            audio.close()

bot.polling(none_stop=True)