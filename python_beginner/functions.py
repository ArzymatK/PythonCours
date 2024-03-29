"""Function"""
# print('Hello World')
# max([1,2,3])

# num1 = 10
# print(num1 + 20 / 5)


# def add_and_devide(x):
#     print(x + 20 / 5)

# add_and_devide(10)

# add_and_devide(20)

# add_and_devide(30

# функция это именнной блок кода коьорый приимает какие-дибо значения, совершает над ними определенные действия и возврощает их результат этих действий

# def greet():
#     print('HelloWorld')

# greet()
# greet(10)

# def add(a, b):
#     print(a + b)

# add (20, 40)
# add (20, 50)

# def add2 (num, num2):
#     result = num + num2
#     return result 

# summa = add2(5, 5)
# print(summa)

#имя функции(аргументы)

#папаметры - локальные переменные для функции обьявляются при создании функции

#аргуметны - это значение для функции при вызове. Аргументов моджет быть столько, сколько параметров у функции

# параметры бывают 2 типов обьязательные и не обьяхательные

#аргумент бывают 2 типов 
# обьязательные 
# позициорннные 

# def  add_nums(num1, num2, num3 = 20):
#     return num1 + num2 + num3

# add_nums(10,20)
# add_nums(num3 = 80, num1 = 10, num2 = 30)


"""args, kwargs - arguement, keyword arguements"""
#*args - кортеж позиционных аргументов 
#**kwargs - словарь именуеммых аргументов

# def func(*args, **kwargs):
#     print(args, '<-args')
#     print(kwargs, '<-kwargs')

#func(1,2,3)#position
#func(a=1, b=2, c=3)#dictionary

# def sum_nums(*nums):
#     result = 0
#     for i in nums:
#         try: 
#             result == i
#         except:
#             print(f"{i} NaN")
#         return result

# def get_names(**contacts):
#     for key, value in contacts.items():
#         print(f"Number {value} belongs to {key}")

# get_names(Kasym=9777777, Arzyma=99999999)

# """ functions - функции """

# print('Hello World')
# max([1, 2, 3])

# num1 = 10
# print(num1 + 20 / 5)

# num2 = 20
# print(num2 + 20 / 5)

# num3 = 30
# print(num3 + 20 /5)

# def add_and_divide(x):
#     print(x + 20 / 5)

# add_and_divide(10)
# add_and_divide(20)
# add_and_divide(30)

# функция - именнованный блок кода, который принимает какие-либо значения, совершает над ними определенные действия и возвращает результат этих действий

# def greet():
#     print('Hello World')

# greet()
# greet(10)

# def add(a, b):
#     print(a + b)

# add(20, 40)
# add(20, 50)
    
# def add2(num, num2):
#     result = num + num2
#     return result

# summa = add2(5, 5)
# print(summa)

# def func():
#     print('this is func')
#     return

# имя_функции(аргументы)

# параметры - локальные переменные для функции, объявляются при создании функции

# аргументы - это значение для функции при вызове. Аргументов может быть столько, сколько параметров у функции

# return - ключевое слово, которое служит для возвращения результат выполнения функции. Является точкой выхода из функции


# def function (*args):
#     for i in args:
#         print(i)

# function(1,2,3,4 )

# def function(**kwargs):
#     for name, value in kwargs.items():
#         print(f'{name} = {value}')
 
# function(a=1, b=2, c=3, d=4)

def sum(*args):
    result = 0 
    for arg in args:
        result += arg 
    return result

print(sum(1,2,3))
print(sum(1,2,3,4))
print(sum(1,2,3,4,5))