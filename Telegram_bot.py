import random


import telebot
from telebot import types

token = '1486393785:AAFyRhngW7aSvkjpXha5AQMb00BAzD-K9ZA'

bot = telebot.TeleBot(token)

keyboard = types.InlineKeyboardMarkup()
key_random = types.InlineKeyboardButton(text='Случайная задача', callback_data='random')
keyboard.add(key_random)


todos = {}

RANDOM_TASKS = ['Написать Гвидо письмо', 'Выучить Python', 'Записаться на курс в Нетологию',
                'Посмотреть 4 сезон Рик и Морти']

HELP = '''
Список доступных команд:
 /print  - напечать все задачи на заданную дату
 /add - добавить задачу
 /help - Напечатать help
 /random - Добавить на сегодня случайную задачу
'''


def add_todo(date, task):
    if date in todos:
        todos[date].append(task)
    else:
        todos[date] = [task]
    print(f'Задача {task} добавлена на дату {date}')


@bot.message_handler(commands=['help'])
def help(message):
    if message.text == '/help':
        bot.send_message(message.chat.id, HELP)
        bot.send_message(message.chat.id,'Поможет выбрать план на сегодня', reply_markup = keyboard)

    elif message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет! Я еще маленький и не все умею, напиши /help')


@bot.message_handler(commands=["add"])
def add(message):
    splitted_command = message.text.split(maxsplit=2)
    date = splitted_command[1].lower()
    task = splitted_command[2]
    if len(task) < 3:
        bot.send_message(message.chat.id, f'Задача {task} не подходит, попробуйте еще раз ')
    else:
        add_todo(date, task)
        bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')


@bot.message_handler(commands=["print"])
def print_tasks(message):
    splitted_command = message.text.split()
    date = splitted_command[1].lower()
    text = ''
    if date in todos:
        for task in todos[date]:
            text = text + f"[ ] {task}\n"
    else:
        text = 'Такой даты нет'
    bot.send_message(message.chat.id, text)

@bot.callback_query_handler(func=lambda call: True)
def random_task(call):
    if call.data == 'random':
        task = random.choice(RANDOM_TASKS)
        add_todo('сегодня', task)
        bot.send_message(call.message.chat.id, f'Задача {task} добавлена на дату сегодня')


bot.polling(none_stop=True)
