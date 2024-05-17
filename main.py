import telebot
import random
from telebot import types
from cfg import token2

bot = telebot.TeleBot(token2)
variant = ['✂ Ножницы', '📜 Бумага', '🗿 Камень']
win = [
    'Ты победил! \nА ты неплохо играешь',
    'Ты победил! \nТвоя удача на высоте',
    'Ты победил! \nНе радуйся так долго'
]
lose = [
    'Ты проиграл! \nЯ превзойду тебя во всём',
    'Ты проиграл! \nЯ лучше людишек',
    'Ты проиграл! \nМашины - 1 людишки - 0',
    'Ты проиграл! \nЯ умнее тебя,у меня памяти 16 мб'
]
draw = [
    'Ничья! \nЯ гитлер',
    'Ничья! \nНикто не победил, как жаль',
    'Ничья! \nПобедила - дружба',
    'Ничья! \nМы не победили, но и не проиграли'
]


def game(user_choice):
    bot_choice = random.choice(variant)
    if user_choice == bot_choice:
        return 'Draw'
    if user_choice == '✂ Ножницы':
        if bot_choice == '📜 Бумага':
            return 'Win'
        if bot_choice == '🗿 Камень':
            return 'Lose'
    if user_choice == '📜 Бумага':
        if bot_choice == '🗿 Камень':
            return 'Win'
        if bot_choice == '✂ Ножницы':
            return 'Lose'
    if user_choice == '🗿 Камень':
        if bot_choice == '✂ Ножницы':
            return 'Win'
        if bot_choice == '📜 Бумага':
            return 'Lose'


@bot.message_handler(commands=['start', 'старт'])
def start(message):
    bot.reply_to(message,
                 '''Приветствую вас дорогой ползователь. Я рад вас приветствовать в нашей игре 《Кам Нож Бум》. Ознакомтесь с правилами и играйте со мной с удовольствием!'
Команда /play начинает игру
Команда /rules показывает правила''')


@bot.message_handler(commands=['help', 'помощь','rule','rules'])
def rules(message):
    bot.send_message(message.chat.id,'''Победитель определяется по следующим правилам:
Бумага побеждает камень («бумага обёртывает камень»).
Камень побеждает ножницы («камень затупляет ножницы»).
Ножницы побеждают бумагу («ножницы разрезают бумагу»).''')


@bot.message_handler(commands=['play'])
def play(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🗿 Камень")
    btn2 = types.KeyboardButton("✂ Ножницы")
    btn3 = types.KeyboardButton("📜 Бумага")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     'Отлично,сейчас вам нужно выбрать и нажать на одну из трех кнопок',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def choice(message):
    if game(message.text) == 'Win':
        bot.send_message(message.chat.id, random.choice(win))
    elif game(message.text) == 'Draw':
        bot.send_message(message.chat.id, random.choice(draw))
    elif game(message.text) == 'Lose':
        bot.send_message(message.chat.id, random.choice(lose))
    else:
        print(message.text)
        print(game(message.text))


bot.polling()
