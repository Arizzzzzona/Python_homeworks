import random

HELP = ''' 
 *help - напечатать справку по программе
 *todo - добавить задачу
 *print - напечатать все задачи
 *random - добавить на сегодня случайную задачу
  '''
Todos = {}

RANDOM_TASK = 'Выучить Python!'
RANDOM_TASKS = ['Выучить Python!','Посмотреть сериал', 'Сделать уборку!']
random_task = random.choice(RANDOM_TASKS)
stop = True

def add_todo(date, task):
    if date in Todos:
        Todos[date].append(task)
    else:
        Todos[date] = [task]
    print(f'Задача {task} добавлена на дату {date}')


while stop:
    command = input('Введите команду: ')
    command.lower()
    if command == 'help':
        print(HELP)
    elif command == 'todo':
        date = input('Когда вы хотите выполнить задачу? ')
        task = input('Введите задачу: ')
        date = date.lower()
        add_todo(date, task)

    elif command == 'print':
        d = input('Введите дату для которой напечатать задачи: ')
        if d in Todos:
            task_list = Todos[date]
            for task in task_list:
                print(f'[] {task}')
        else:
            print('Такой даты нет')

    elif command == 'random':
        add_todo('сегодня', random_task)

    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        stop = False

    else:
        print('Неизвестная команда')

