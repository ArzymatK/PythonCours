# 8 основных типов данных

# 1)int - целый числовой вид данных (1,2,3,4,5)
#      float - числа с плавающей точкой 
#       complex - числа с буквенным вырожением (1234567789n)
# 2) str - строковой тип данных - "Строка"
# 4) bool - булевой тип данных / логические (правдв / ложь)
# 4) list - список []
# 5) touple - кортеж / неизменный список
# 6) set - множество {}
#7) dict - словарь []
#8) Nonetype - тип данных для обозночения отсутствия
   

#Изменяемые вмиды данных (moutable)
# list 
# dict
# set

# print("Hello World") # print() функция для вывщда содержимого на терминал
# name=input("Введите ваше имя:")
# print("Hello," + name)

# """ Hello how are you Bakdoolot """
# print("Hello\nHow are you")

#  str1 = 'Hello'
#  str2 = 'world'
#  print(str1 +str2)

#  frog = 'Quak'
#  print(frog * 3) #QuakQuakQuak

#  """ Функции и методы строк """

#  greeting = "Good evening"

#  print(len(greeting))

 #print(len(greeting))
 #len(x) - возврощает количество элементов

#  print(dir(greeting))
 #dir(x) - возврощает список методов переданного обьекта

 # Метод - функция, принадлежэащяя определенному типу данных, и может быть связана вызывапна только через объект

# my_str = 'Hello world'

# print(my_str.lower())#
# print(my_str.upper()) #
# print(my_str.replace('#','')) #
# print(my_str.split('#')) #Делит строку по разделителю

# my_str2 = '  hello world  '

# my_str2.title() #Hello World

# my_str2.count("l") #3

# print(my_str2.strip()) #удаляет лимшние пробелы

# my_str2.lstrip()
# my_str2.rstrip()

# print(my_str2.strip('!'))

# my_str3 = 'My new String'

# my_str3.isalpha() #True
# my_str3.isdigit() #False
# my_str3.isalnum() #False
# my_str3.endswith('M') #False

# in

# my_str4 = 'Hello world'

# print('Hello' in my_str4)

# 'Hello' in my_str4 #True

# name = input('Name:')
# party = input('Meeting:')

# invite1 = 'Дорогой %s, пригшлашаем тебя на %s' % (name, party)
# print(invite1)
# invite2 = 'Дорогой {al}, приглашаем тебя на {b2}'.format(al=name, b2=party)

# invite3 = f'Дорогой {name}, приглашаем тебя на {party}'
# print(invite3)

# 'Python'

# print(String[4])
# print(string[::-2])

#string[start:stop:step]
