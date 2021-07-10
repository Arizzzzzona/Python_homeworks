TaskM = {}
print ('Введите дату: ')
date1 = input()
print("Введите задачу: ")
task1 = input()

print ('Введите дату: ')
date2 = input()
print("Введите задачу: ")
task2 = input()

print ('Введите дату: ')
date3 = input()
print("Введите задачу: ")
task3 = input()

print(date1 + ' ' + task1)
print(date2 + ' ' + task2)
print(date3 + ' ' + task3)

TaskM[date1, date2, date3] = task1, task2, task3
print(TaskM)
