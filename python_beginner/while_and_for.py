"""While"""

#while условное выражения:
# Игструкции 
# number = 1 

# while number < 5:
#     print(f'number = {number}')
#     number += 1
# print("Рабоиа завершена")

# while number < 0:
#     print(f'number = {number}')
#     number += 1
# print("Рабоиа завершена")
# else:   
#     print("don't work")
#     print()

# my_list = [1,2,3,4,5,6,7,8,9,10]
# index = 0 

# while my_list[index] != 5:
#     print(my_list[index])
#     index += 1
 #принтит все числа пока не достигнет 5:


# total = 0  # (0 + 1, 1+2, 3+3)
# num  = 1 #(1 + 2 + 3 + 4 +5)

# while num <= 100:
#     total += num
#     num += 1
# print(total)

###Вложенные циклы 

# i = 1
# j = 1

# while i < 10:
#     while j < 10:
#         print(i * j, end="")
#         j += 1
#     print("\n")
#     j = 1
#     i += 1 

"""For"""
 
# for переменная in набор значений:
#     Инструкции

# messege = 'Hello'

# for c in messege:
#     print(c)
    # c пробегается по всему значению messege и принтит его по буквам 
 
# for n in range (4,10):
#     print(n, end="")#принтит от 4 до 10

# for n in range (0, 10, 2):
#     print(n)

# for n in range (0, 10, 2):
#     print(n)
# else:
#     print(f'Last number {n}')

# for c1 in "ab":
#     for c2 in "ba":
#         print(f"{c1}{c2}")
        #print  aa ab bb ba

"""break, continue"""

# number = 0 

# while number <  5:
#     number += 1
#     if number == 3:
#         break
#     print(f"number = {number}")
    #принтит пока не достигнет 3 break останавливает процесс

# number = 0 

# while number <5:
#     number += 1
#     if number == 3:
#         continue
#     print(f"number = {number}")
    #принтит до 5 continue который теперь стоит вместо продолжает процесс пока number < 5:

# s = 0

# for i in range(-10, 101): #for i in range(-10, 101):#for i in range(-10, 1): 
#     if i == 0:
#         break
#     s += 1/i 
# else:
#     print("Суммы вычислены коректно")

# print(s)

# a = [1,2,3,4,5]

# for i, v in enumerate(a):
#     print(i, v)

# for i in enumerate(a):
#     print(i)

# for i in range(2, 10, 2):
#     print(i)

# while True:
#     a = int(input("Введите чияло"))
#     b = int(input("Введите второе число"))
#     if a == 0 or b == 0:
#      break
#     print(a + b)


# top = ['Arzymat','Kasym','Jackie','Tima']

# for i, v in enumerate(top):
#     print(i, v)
  
# num = [1,2,3,4,5,6,7,8,9,10]


# number = 1

# while number <= 5:
#     if number != 3:
#         # continue
#         print(number)
#     number += 1
b = int(input"Введите число")

for b in range (2, 10):
    if b // range (2,4,6,8,10):
     print('Good')
    else:
        print('bad')
    

# for n in range (4,10):
#     print(n, end="")#принтит от 4 до 10

# for n in range (0, 10, 2):
#     print(n)

# for n in range (0, 10, 2):
#     print(n)
# else:
#     print(f'Last number {n}')