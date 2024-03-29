#"""Упаковка и расспаковка в параметрах функций"""
# """args""" and """kwargs"""

# def fun(*args):
#     print(args[0])

#     print(args)

# fun("pythn", "C++", "Java", "C")




# def sum(*args):
#     result = 0 
#     for arg in args:
#         result += arg 
#     return result

# print(sum(1,2,3))
# print(sum(1,2,3,4))
# print(sum(1,2,3,4,5))




# def fun(**kwargs):
#     print(kwargs)
#     for key in kwargs:
#         print(f'{key} = {kwargs[key]}')

# fun(name = "Alex", age = 24, company = "KyrgyzCode")
# fun(language = "python", version = "3.10")




# def sum(*args):
#     result = 0 
#     for arg in args:
#         result += arg
#     return result

# numbers = (1,2,3,4,5)
# print(sum(*numbers)) #*Распаковка




# def print_person(name, age, company):
#     print(f'Name: {name}, age: {age}, company: {company}')

# person = ("Alex", 24, "KyrgyzCode")
# print(*person)




#Распаковка




# def print_person(name, age, company):
#      print(f'Name: {name}, age: {age}, company: {company}')

# person = {'Name': 'Alex', "age": 24, "company":"KyrgyzCode"}
# print(**person)

# def sum(num1, num2, *nums):
#     result = num1 + num2
#     for n in nums:
#         result += n
#     return result

# print(sum(1,2,3))
# print(sum(1,2,3,4))\




# def list_appender(list1, list2, *args):
#     my_list = []

#     my_list.append(list1)
#     my_list.append(list2)

#     if args:
#         my_list.append(args)
#     return my_list



# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]
# l3 = ['word', 'age', 'salary']

# print(list_appender(l1,l2,l3))

# num = 10 
# print(num + 20 / 5)

# num2 = 20 
# print(num2 + 20 / 5)




"""lambda - вырожения предстовлдяют небольшие анонимные функции которыек определяются с помощью оператора lambda """



# def messege():
#     print("Hello")

# messege = lambda: print("Hello")

# messege()

# square = lambda n: n * n 

# print(square(4))
# print(square(5))
    
# sum = lambda a, b: a + b





# def do_operation(a,b, operation):
#     result = operation(a,b)
#     print(f'result = {result}')

# do_operation(5,4, lambda a, b: a +b)
# do_operation(5,4, lambda a , b: a * b)






# numbers = [1,2,3,4,5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers) #MAP - присваивается к каждому элементу в переменной





# numbers = [1,2,3,4,5]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)#Filter






# def select_operator(choice):
#     if choice == 1:
#         return lambda a, b: a + b
#     elif choice == 2:
#         return lambda a, b: a - b
#     else: 
#         return lambda a, b: a * b
# operation = select_operator(1)
# print(operation(10, 6))

# operation = select_operator(2)
# print(operation(10, 6))

# operation = select_operator(3)
# print(operation(10, 6))


 
# def select_operator(choice):
#     if choice == 1:
#         return lambda a, b, c: a * b * c
# operation = select_operator(1)
# print(f'Обьем бассейна: {operation(20, 40, 55)}')



# Написать lambda которая принимает 3 параметра и умножает все параметры между собой. 
# Функция должна вернуть строку: "Объём бассейна " и значение которое получилось