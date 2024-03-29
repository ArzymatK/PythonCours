# """Множество 'set'"""
# my_set = {1,2,3,4, 1}
# print(my_set)

# class_js = {'Aktan', 'Aygul', 'Mayrash', 'Artyom'}
# class_python = {'Malik', 'Aygul', 'Eldos', 'Aktan'}

# # inter = class_js.intersection(class_python)
# # print(inter)
# # print(class_js & class_python)

# diff = class_js.difference(class_python)
# diff2 = class_python.difference(class_js)
# # print(class_js - class_python)
# # print(diff)
# # print(diff2)

# # print(class_js.union(class_python))
# # print(class_js | class_python)

# fruits  = {'apple', ' banana', 'Kiwi', 'tangerin'}
# vegetables = {'carrot', 'potato', 'Tomato', 'apple'}

# friuts.intersection_update(vegetables)
# print(fruits)
# print(vegetables)

# fruits.difference_update(vegetables)
# print(fruits)

# my_set = {(1,2,3) '123132'}, 

# my_set.remove('123132')
# my_set.discard('123132')
#my_set.pop()
# print(my_set)

# """Словари {dicts}"""

# passport = {'name': 'Meerim', 'last_name': 'Kayratove', 'age':25, 'gender':'F'}
# print(passport['name'])
# print(passport['last_name'])
# print(passport['age'])

# passport['license'] = 'Can drive B'
# passport['license'] = "Can drive A"
# # print(passport)

# # print(dict(name='Islam', age=22))
# # print(dict([
# #     ('name', 'Baimurat')
# #     ('age', 25)
# # ]))

# new_dict = dict.fromkeys(['a', 'b'], 10)
# # print(new_dict)

# new_dict = {
#     'name': 'Ak maral'
#     []
# }

# dicts = {
#     'dict1' : 
# }

# car = {
#     "marka": "Tayota"
#     "model": "Camry"
#     "color": "black"
#     "volume": "3.2"
#     "year": "2012"
#     'kuzov': 'Kupe'
# }

# new_dict = dict.fromkeys(['a', 'b'], 10)
# # print(new_dict)

# # new_dict = {
# #     True: 'Ak-Maral',
# #     [1, 2, 3, 4]: 'ERRORRROR'
# # }

# dicts = {
#     'dict1': {'name': 'Islamchik', 'age': 190},
#     'dict2': [1, 2, 3, 4]
# }
# # print(dicts)

# # print(dicts['dict1']['name'])


# car = {
    # "marka": "Toyota",
    # "model": "Camry",
    # "color": "black",
    # "volume": 3.2,
    # "year": 2012,
    # 'kuzov': 'Купе'
# }

# print(car['marka'])
# print(car['kuzov'])

# print(car.get('kuzov', 'ТАКОГО КЛЮЧА НЕТ'))

# print(car.setdefault('kuzov', 'Седан'))

# house = {
#     "color": "white",
#     "category": "elite",
#     "rooms": 4,
#     "warmness": True
# }

# house['area'] = '30x40'
# print(house)

# house.update({'floor': 2, 'door': 'wooden'})
# print(house)

# my_list = [
#     ['street', 'chuyskaya'], 
#     ['garage', False]]

# house.update(my_list)
# print(house)

# category = house.pop('category')
# print(category)
# print(house)

# garage = house.popitem()
# print(garage)

# del house['area']

# game = {
#     'title': 'Fable The Lost Chapters',
#     'year': 2006,
#     'author': 'Peter',
#     'category': 'RPG'
# }

# # print(list(game.values()))
# # print(list(game.keys()))

# # print(list(game.items()))

# couple = ('title', 'Fable The Lost Chapters', 'The')
# k, v, t = couple
# print(f'Ключ: {k}\nЗначение: {v}\n{t}')

# human = {
#     'name': 'Aliya', 
#     'age': 22,
#     'gender': 'F',
#     'friends': ['Melis', 'Begimay']
# }


# human2 = human.copy()
# # print(human2['age'] == human['age'])
# # print(human2['age'] is human['age'])

# from copy import deepcopy

# human3 = deepcopy(human)
# print(human3['friends'] == human['friends'])


# names = ['Islamchic', 'Aleks', 'Niyaz']

# print('Baimurat' in names)


# person = {
#     'name': 'Abdul',
#     'age': 22,
#     'passport': {
#         'name': 'Abdul',
#         'ID': 21753129364,
#         'nationality': 'kyrgyz'
#     },
#     'drive_license': {
#         'category': 'B',
#         'year': 2011
#     }
# }

# print(person['passport']['nationality'])



# my_set=[1,2,3,4,5,6,7,8,9,]
# my_set.pop(6)
# print(my_set)

# set1 = ['23' '46' '56' '32']
# set2 = ['98' '23' '101' '56']
# diff = set_1.difference(set_2)
# diff2 = set_2.difference(set_1)
# print(set_1 - set_2)
# print(diff)
# print(diff2)

# set1 = {1,2,3,4,5}
# set2 = {1,2,3,4,}
# set1.intersection_update(set2)
# print(set1)



# diff = class_js.difference(class_python)
# diff2 = class_python.difference(class_js)
# print(class_js - class_python)
# print(diff)
# print(diff2)


# set2 = {1,2,3,4,5}
# set3 = {1,2,3,4,}
# set2.difference_update(set3)
# print(set2)

# x = [1,2,3,4,5,6,7]
# x.pop()
# print(deleted_element)


# fruits.difference_update(vegetables)
# print(fruits)

# person = {
#     'name': 'Abdul',
#     'age': 22,
#     'passport': {
#         'name': 'Abdul',
#         'ID': 21753129364,
#         'nationality': 'kyrgyz'
#     },
#     'drive_license': {
#         'category': 'B',
#         'year': 2011
#     }