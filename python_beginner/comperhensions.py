'''Генераторы9(comprehemsion)'''

# list_ = []
# for i in range(1,6):
#     list_.append(i)
# print(list_)

# list_ = [i for i in range(1,6)]
# print(list_)

# comprehemsion - короткий способ записи циклов для создания коллекцияй 


# синтаксис генератора =  [вырожения с переменной for переменная in интерируемый обьект]

"""comprehemsion"""

# nums = [i for i in range(1, 10)]
# print(nums)

# nums_10 = []
# for i in range(1,6):
#     nums_10.append(i+10)

""" comporehesions (генераторы) """

# list_ = []
# for i in range(1, 6):
#     list_.append(i)
# print(list_)

# list_ = [i for i in range(1, 6)]
# print(list_)

# comprehensions - короткий способ записи циклов для создания коллекций

# синтаксис_генератора = [выражение_с_переменной for переменная in итерируемый объект]

""" list (comprehensions) """
# 1) добавить в список 10 чисел от 1 до 10
# nums = []

# for i in range(1, 10):
#     nums.append(i)

# print(nums)

# nums = [i for i in range(1, 10)]
# print(nums)

# 2) записать в список числа в диапазоне от 1 до 6, при этом к каждому числу добавить +10

# nums_10 = []
# for i in range(1, 6):
#     nums_10.append(i+10)

# print(nums_10)

# nums_10 = [i + 10 for i in range(1,6)]
# print(nums_10)

# 3) Записать в список числа в диапазоне от 1 до 10, при этом только те, которые являются четными
# even_nums = []

# for i in range(1, 10):
#     if i % 2 == 0:
#         even_nums.append(i)

# print(even_nums)

# even_nums = [i for i in range(1, 10) if i % 2 ==0]

# print(even_nums)

# names = ['Arzymat', 'Kasym', 'Islam']
# students = [name+' Python' if name == 'Arzymat' else name for name in names]
# print(students)

# синтаксис_генератора_с_условием = [выражение for выражение in итерируемый_объект if условие]

# 4) Записать в список числа в диапазоне от 1 до 10, при этом к четным прибавлять по 10, к нечетным по 200

# numbers = [num + 10 if num % 2 == 0 else num + 200 for num in range(1, 10)]
# print(numbers)

# numbers = []
# for num in range(1, 10):
#     if num % 2 == 0:
#         numbers.append(num+10)
#     else:
#         numbers.append(num+200)

# print(numbers)


# синтаксис_генератора_с_двумя_условиями = [тернарный оператор for выражениe in итерируемый_объект]

# 4) Записать в список числа в случайном диапазоне, к четным прибавить 10, к нечетным прибавить 200, но работать только с теми числами, которые больше 5

# import random
# random_num = random.randrange(5, 20)

# nums = []
# for num in range(1, random_num):
#     if num > 5:
#         if num % 2 == 0:
#             nums.append(num+10)
#         else:
#             nums.append(num+200)
#     else:
#         print(num)

# print(nums)

# numbers = [num + 10 if num % 2 == 0 else num + 200 for num in range(1, 10) if num > 5]

# print(numbers)

# nums = []
# for num in range(1, 10):

#     for a_num in range(10, 20):
#         nums.append(num + a_num)
#         [11, 12, 13, 14, 15, 16, 17, 18, 19, 20,]

#     # nums.append(num + 1)
# print(nums)


# nums = [num + a_num for num in range(1, 10) for a_num in range(10, 20)]
# print(nums)

""" set (comprehensions) """

# my_set = {i for i in range(1, 10)}
# print(my_set)

""" tuple (comprehensions) """

# my_tuple = tuple(i for i in range(1, 10))
# print(my_tuple)

# """ dict (comprehensions) """

# names = {
#     'Arstan': 22,
#     'Mirbek': 24,
#     'Aliya': 21
# }

# aged_names = {}
# for key, value in names.items():
#     aged_names.update({key: value + 1})

# print(aged_names)

# aged_names = {key: value + 1 for key, value in names.items()}
# print(aged_names)
# print(names.items())

# for key, value in [('Arstan', 22)]:
#     print(key, value)

""" comporehesions (генераторы) """

# list_ = []
# for i in range(1, 6):
#     list_.append(i)
# print(list_)

# list_ = [i for i in range(1, 6)]
# print(list_)

# comprehensions - короткий способ записи циклов для создания коллекций

# синтаксис_генератора = [выражение_с_переменной for переменная in итерируемый объект]

""" list (comprehensions) """
# 1) добавить в список 10 чисел от 1 до 10
# nums = []

# for i in range(1, 10):
#     nums.append(i)

# print(nums)

# nums = [i for i in range(1, 10)]
# print(nums)

# 2) записать в список числа в диапазоне от 1 до 6, при этом к каждому числу добавить +10

# nums_10 = []
# for i in range(1, 6):
#     nums_10.append(i+10)

# print(nums_10)

# nums_10 = [i + 10 for i in range(1,6)]
# print(nums_10)

# 3) Записать в список числа в диапазоне от 1 до 10, при этом только те, которые являются четными
# even_nums = []

# for i in range(1, 10):
#     if i % 2 == 0:
#         even_nums.append(i)

# print(even_nums)

# even_nums = [i for i in range(1, 10) if i % 2 ==0]

# print(even_nums)

# names = ['Arzymat', 'Kasym', 'Islam']
# students = [name+' Python' if name == 'Arzymat' else name for name in names]
# print(students)

# синтаксис_генератора_с_условием = [выражение for выражение in итерируемый_объект if условие]

# 4) Записать в список числа в диапазоне от 1 до 10, при этом к четным прибавлять по 10, к нечетным по 200

# numbers = [num + 10 if num % 2 == 0 else num + 200 for num in range(1, 10)]
# print(numbers)

# numbers = []
# for num in range(1, 10):
#     if num % 2 == 0:
#         numbers.append(num+10)
#     else:
#         numbers.append(num+200)

# print(numbers)


# синтаксис_генератора_с_двумя_условиями = [тернарный оператор for выражениe in итерируемый_объект]

# 4) Записать в список числа в случайном диапазоне, к четным прибавить 10, к нечетным прибавить 200, но работать только с теми числами, которые больше 5

# import random
# random_num = random.randrange(5, 20)

# nums = []
# for num in range(1, random_num):
#     if num > 5:
#         if num % 2 == 0:
#             nums.append(num+10)
#         else:
#             nums.append(num+200)
#     else:
#         print(num)

# print(nums)

# numbers = [num + 10 if num % 2 == 0 else num + 200 for num in range(1, 10) if num > 5]

# print(numbers)

# nums = []
# for num in range(1, 10):

#     for a_num in range(10, 20):
#         nums.append(num + a_num)
#         [11, 12, 13, 14, 15, 16, 17, 18, 19, 20,]

#     # nums.append(num + 1)
# print(nums)


# nums = [num + a_num for num in range(1, 10) for a_num in range(10, 20)]
# print(nums)

""" set (comprehensions) """

# my_set = {i for i in range(1, 10)}
# print(my_set)

""" tuple (comprehensions) """

# my_tuple = tuple(i for i in range(1, 10))
# print(my_tuple)

""" dict (comprehensions) """

names = {
    'Arstan': 22,
    'Mirbek': 24,
    'Aliya': 21
}

# aged_names = {}
# for key, value in names.items():
#     aged_names.update({key: value + 1})

# print(aged_names)

# aged_names = {key: value + 1 for key, value in names.items()}
# print(aged_names)
# print(names.items())

# for key, value in [('Arstan', 22)]:
#     print(key, value)
""" comporehesions (генераторы) """

# list_ = []
# for i in range(1, 6):
#     list_.append(i)
# print(list_)

# list_ = [i for i in range(1, 6)]
# print(list_)

# comprehensions - короткий способ записи циклов для создания коллекций

# синтаксис_генератора = [выражение_с_переменной for переменная in итерируемый объект]

""" list (comprehensions) """
# 1) добавить в список 10 чисел от 1 до 10
# nums = []

# for i in range(1, 10):
#     nums.append(i)

# print(nums)

# nums = [i for i in range(1, 10)]
# print(nums)

# 2) записать в список числа в диапазоне от 1 до 6, при этом к каждому числу добавить +10

# nums_10 = []
# for i in range(1, 6):
#     nums_10.append(i+10)

# print(nums_10)

# nums_10 = [i + 10 for i in range(1,6)]
# print(nums_10)

# 3) Записать в список числа в диапазоне от 1 до 10, при этом только те, которые являются четными
# even_nums = []

# for i in range(1, 10):
#     if i % 2 == 0:
#         even_nums.append(i)

# print(even_nums)

# even_nums = [i for i in range(1, 10) if i % 2 ==0]

# print(even_nums)

# names = ['Arzymat', 'Kasym', 'Islam']
# students = [name+' Python' if name == 'Arzymat' else name for name in names]
# print(students)

# синтаксис_генератора_с_условием = [выражение for выражение in итерируемый_объект if условие]

# 4) Записать в список числа в диапазоне от 1 до 10, при этом к четным прибавлять по 10, к нечетным по 200

# numbers = [num + 10 if num % 2 == 0 else num + 200 for num in range(1, 10)]
# print(numbers)

# numbers = []
# for num in range(1, 10):
#     if num % 2 == 0:
#         numbers.append(num+10)
#     else:
#         numbers.append(num+200)

# print(numbers)


# синтаксис_генератора_с_двумя_условиями = [тернарный оператор for выражениe in итерируемый_объект]

# 4) Записать в список числа в случайном диапазоне, к четным прибавить 10, к нечетным прибавить 200, но работать только с теми числами, которые больше 5

# import random
# random_num = random.randrange(5, 20)

# nums = []
# for num in range(1, random_num):
#     if num > 5:
#         if num % 2 == 0:
#             nums.append(num+10)
#         else:
#             nums.append(num+200)
#     else:
#         print(num)

# print(nums)

# numbers = [num + 10 if num % 2 == 0 else num + 200 for num in range(1, 10) if num > 5]

# print(numbers)

# nums = []
# for num in range(1, 10):

#     for a_num in range(10, 20):
#         nums.append(num + a_num)
#         [11, 12, 13, 14, 15, 16, 17, 18, 19, 20,]

#     # nums.append(num + 1)
# print(nums)


# nums = [num + a_num for num in range(1, 10) for a_num in range(10, 20)]
# print(nums)

""" set (comprehensions) """

# my_set = {i for i in range(1, 10)}
# print(my_set)

""" tuple (comprehensions) """

# my_tuple = tuple(i for i in range(1, 10))
# print(my_tuple)

""" dict (comprehensions) """

# names = {
#     'Arstan': 22,
#     'Mirbek': 24,
#     'Aliya': 21
# }

# aged_names = {}
# for key, value in names.items():
#     aged_names.update({key: value + 1})

# print(aged_names)

# aged_names = {key: value + 1 for key, value in names.items()}
# print(aged_names)
# print(names.items())

# for key, value in [('Arstan', 22)]:
#     print(key, value)


# a = int(input('Введите число'))
# if a % 1 == 0 and a % a == 1:
#     print('Простое')
# else:
#     print('Не простое')
# print(a)

