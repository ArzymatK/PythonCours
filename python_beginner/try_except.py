""" try except - ошибки и исключения в python """

# исключения - проблема в логике работы кода
# ошибка - проблема в написании кода / синтаксисе кода

#a = 10
#b = 20
# print(c)

#NameError # исключение отсутствия имени

# 10 / 0
#ZeroDivisionError # исключение при делении на ноль

# names = {'Aleks': True, 'Baimurat': 'Front'}
# names['Islam']
#KeyError # исключение ключа

# list_ = [1, 2, 3]
# list_[5]
#IndexError # индекс не входит в диапазон списка

# string = input('Введите число: ')
# num = int(string)
# print(num ** num)
#ValueError # ошибка значения. Когда тип объекта может подходить под условие, но его значение нет

# num = 10
# num + 'string'
#TypeError # ошибка типов данных, когда тип объекта не подходит для операции

#string = 'hello world'
# string.append('b')
#AttributeError # отсутствие атрибута или метода у объекта

# import wrong_import
#ModuleNotFoundError # отсутствие модуля

# from math import wrong_func
#ImportError # неверный импорт

# Ошибки

# for i in range(10)
#     print(i)
#SyntaxError # синтаксическая ошибка


# for i in range(10):
# print(i)
#IndentationError # ошибка отступа

# for i in range(10):
#      print(i)
#TabError # ошибка табуляции (смешивание табов и пробелов)


#contacts = {
#    'Alex': 32913912,
#    'Baika': 2819312
#}

# contacts['Islam']
# print('Hello')



# try except - конструкция для обработки исключений
# try:
#     contacts = {
#         'Alex': 28312839132,
#         'Baika': 18239183129
#     }
#     contacts['Islam']

# except:
#     print('Нет такого имени')

# print('Hello')

# try:
#     print('Hello')
#     10 / 0
#     print('World')
# except:
#     print('что то пошло не так')
# else:
#     print('Try отработал без ошибок')
# finally:
#     print('Я отработаю в любом случае')

# nums = [1, 2, 3, 4]
# try:
#     a = nums[-1]
#     nums[10]
# except IndexError:
#     print('Возникла ошибка')

#try:
    # print(c)
    # 10 / 0
    # 'string.'.extend()
#    pass
#except (NameError, ZeroDivisionError):
#    print('Нет такого имени и нельзя делить на ноль')
#except AttributeError:
#    print('Нет такого атрибута')


#Exception
# try:
#     print(m)
# except Exception as error:
#     print(error)


# try:
#     код, который потенциально вызвать исключение
# except:
#     блок кода, который сработает, если в try было вызвано исключение
# else:
#     выполняется если в try не было исключений
# finally:
#     выполняется в любом случае

# raise - ключевое слово для поднятия/вызова ошибок
# money = 0
# if money == 0:
#     raise ValueError('Недостаточно денег на карте')

# try:
#     raise Exception('Моя ошибка')
# except Exception:
#     print('ошибка обработана')
# finally:
#     print('Программа завершена')


# try:
#     for i in range(10)
#         print(i)
# except SyntaxError:
#     print('неправильно написан код')


#contacts = {'Aleha': 3883, 'Ivan': 2833, 'Aliya': 4783}
# try:
#     name = input('Введите имя ').title()
#     contacts[name]
# except KeyError:
    # print('Нет такого имени')

# name = input('Введите имя: ').title()
# if name not in contacts:
#     print('Нет такого имени')
# else:
#     contacts[name]

# print(contacts.get('Nur', 'Нет такого имени'))

#class IslamFrontendError(Exception):
#   print('JavaScript лучше')

# raise IslamFrontendError

#print('hello world'.title()) # -> Hello World
#print('hello world'.capitalize()) # -> Hello world

#HomeWorks
# try:
#     a = input("Enter the number:")
#     b = input("Enter the number:")
#     print(a + b)
# except TypeError:
#     print("TypeError. Error of data types")


# try:
#     my_list = [1,2,3,4,5,6,7,8]
#     print(my_list[3])
# except IndexError:
#     print("IndexError ther is no arguement with such index")


# try:
#     a = 10
#     b = 20
#     print(c)
# except NameError:
#     print("NameError. There is no variable with such name.")


# try:
#     a = int(input("Введите число:"))
#     print(a**2)
# except:
#     print("Ошибка. Вы ввели не число.Советую вернуться в школу и научиться отличать цифры от букв =)")


# try:
#     my_list = [1,2,3,4,'mondo',5,9]
#     total = 0
#     for i in my_list:
#         total += i
#     print(f'Total sum of numders:',{total})
# except TypeError:
#     print:("TypeError. There is smth wrong in the list")


# try: 
#     a = int(input("Enter the number:"))
#     b = int(input("Enter the number:"))
#     print(a/b)
# except:
#     a == 0 or b == 0
#     print("Ошибка. Одно из них ровняется нулю")
# finally:
#     print("Процесс завершен")


# def place_of_index(input_string, index):
#     try:
#         mondo = input_string[index]
#         print(mondo)
#     except IndexError:
#         print(f"Index {index} located out of length")
# _string_ = "Hello mondo"
# _index_ = 8
# res = place_of_index(_string_,_index_)
# print(f"Symbol {_string_} is located on position numder: {_index_}")


# def square_of_num():
#     try:
#         a = int(input("Enter the number:"))
#         if a == True:
#             print(a * a)
#     except TypeError:
#         if a == False:
#             print("TypeError")
# square_of_num()


# def devision_nums():
#     try:
#         a = int(input("Enter the number:"))
#         b = int(input("Enter the number:"))
#         print(a / b)
#     except ValueError:
#         if a or b == NaN:
#             print("Ошибка одно из чисел не является числом")
#     except ZeroDivisionError:
#             print("Ошибка. Одна из чисел ровна 0")
# devision_nums()

