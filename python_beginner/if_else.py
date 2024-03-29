"""Условные вырожения (if-else-elif)"""


# bool() - неизменяемый тип данных, который имеет всего 2 значения: True, False

10 > 2 # True
# > - больше
# < - меньше
# <= - меньше или равно
# >= - больше или равно
# != - неравенство
# == - равенство


# print(25 == 33) # False
# print(25.0 == 25) # True
# print('строка' > 5) # Error

# print(bool(0)) # False
# print(bool(1)) # True
# print(bool(-2)) # True

# print(30 - True) # 29

# print(bool(''))
# print(bool([]))
# print(bool({}))

# num = 10
# if num > 20:
#     print('Num больше 20')
# else:
#     print('Num не больше 20')


# temperature = 40
# if temperature < 20:
#     print('холодно')
# else:
#     if temperature < 30:
#         print('тепло')
#     else:
#         if temperature > 35:
#             print('жарко')


# temperature = 40
# if temperature < 20:
#     print('Холодно')

# elif temperature < 30:
#     print('Тепло')
# elif temperature > 35:
#     print('ЖАРКО')
# else:
#     print('Неверная температура')

# num2 = 15
# if num2 < 20:
#     print('num2 < 20')
# elif num2 > 10:
#     print('num2 > 10')

# grade = input('Введи свою оценку от 1 до 5: ')
# if grade.isdigit():
#     grade = int(grade)
#     if grade == 5:
#         msg = 'Ты молодец'
#     elif grade == 4:
#         msg = 'хз норм'
#     elif grade <= 3:
#         msg = 'Подтянись'
#     else:
#         msg = 'Не умничай'
#     print(msg)
# else:
#     print('Ты ввел не число')

""" and, or, not """
# age = 29
# if age > 18 and age < 29:
#     print('Входите уважаемый')
# else:
#     print('Нет, входа нет')

# krasavchik = False
# grade = 4

# if krasavchik or grade == 5:
#     print('Продолжаешь учится')
# else:
#     print('Отчислен')


# False # False
# True # True

# False and False # False
# True and True # True
# False and True # False
# True and False # False

# False or False # False
# True or True # True
# False or True # True
# True or False # True

# not True # False
# not False # True

# """ is, ==, in """

# string = 'hello worlds'
# print('world' in string) # True


""" Тернарный оператор """
# msg = input('Введите сообщение ')
# if len(msg) > 10:
#     print('Сообщение длиннее 10')
# else:
#     print('Сообщение короче 10')


# msg = input('Введите сообщение ')
# res = 'Сообщение длинне 10' if len(msg) > 10 else 'Сообщение короче 10'
# print(res)

# if условие:
#     действие 1
# else:
#     действие 2


# действие 1 if условие else действие 2

# if условие 1:
#     действие 1
# elif условие 2:
#     действие 2
# else:
#     действие 3


# res = 2**3 < 3**2
# print(res)

num = input('Введите число')
 print(num) 







