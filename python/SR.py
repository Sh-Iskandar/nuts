# -*- coding: utf-8 -*-
import keyword
import random
import pickle
import json
import math

# kwd_to_find="eXcept"
# print(keyword.kwdlist)
# print(list(range(2,10,3)))
# for i in range(0,10,2):
#    print(i)
#    print(len(range(0,10,2)))
# a=[1,2,3,6,8,10]
# a=random.randint(-10,10)
# b=random.randint(-10,10)
# print(f"F-строка Сколько будет (a)+(b)?")
# c=input()
# try:
#    if int (c)==(a+b):
#        print("правильно")
#    else:
#     print("неверно")
# except:
#   print("не правильно ввели число")
# finally:

# while True:
# print("Hello")

# rand=random.randint(-90*10^3,75*10^3);
# print(rand);
# try:
#     user_input=int(input("Введите целое число в диапазоне [-90*10^3,75*10^3] "))
#     if -90000<=user_input<=75000:
#         otv=abs(((rand-user_input)/rand)*100)
#         print(otv)
#     else:
#         print("Введите число в этом диапазоне")
# except:
#    print("не правильно ввели число")
# list="RavaA"
# col='555555'  count,min max,sort
# my_list=[1,2,3,'deadwe',5,6]
# print(my_list.index(3))
# print(list.find('a'))
# print(list.replace('a','b'))
# print(list.upper())
# print(list.lower())
# print(list.isalpha())
# print(int(col))
# print(col.isnumeric())
# #print(type(list))
# print(my_list[1::2])
# my_list.append('88')
# # print(my_list)
# my_list.extend([5,5,5])
# print(my_list)
# my_list.insert(2,'sss')
# print(my_list)
# del my_list[4]
# my_list.remove(2)
# print([my_list]*3)
# matrix=[[1,2,3],[4,5,6]]
# print(matrix[0][0])
# isinstance(list,int)

# det={1:'string1',2:'string2','str3':654}
# for key, value in det.items():
#       print(key,value)
# print(det.get(6,'hjmh'))


# новый_менеджер = {'lastname': 'Смирнов', 'name': 'Алексей', 'middlename': 'Петрович'}
# my_dict['Менеджер'] = my_dict.get('Менеджер', новый_менеджер)
#
# my_dict = {
#     'Директор': {'Фамилия': 'Иванов', 'Имя': 'Иван', 'Отчество': 'Иванович'},
#     'Бухгалтер': {'Фамилия': 'Куликова ', 'Имя': 'Малика', 'Отчество': 'Кирилловна'},
#     'Охрана': {'Фамилия': 'Жуков', 'Имя': 'Сергей', 'Отчество': 'Андреевич'}
# }
#
# def new_worker():
#     lastname = input('Введите фамилию: ')
#     if lastname=="":
#         lastname="Макаров"
#     name = input('Введите имя: ')
#     if name=="":
#         name="Егор"
#     middlename = input('Введите отчество: ')
#     if middlename=="":
#         middlename="Алексеевич"
#     return {'Фамилия': lastname, 'Имя': name, 'Отчество': middlename}
#
#
# def add_new_list():
#     post = input('Введите должность для новой записи: ')
#     while True:
#         new_list = new_worker()
#         print('Новые данные:', new_list)
#         confirm = input('Подтвердите введенные данные (да/нет): ')
#         if confirm.lower() == 'да':
#             my_dict[post] = new_list
#             break
#         else:
#             print('Попробуйте ввести данные заново.')
#
# print('Содержимое словаря до добавления новых записей:')
# for post, info in my_dict.items():
#     print(f'{post}: {info}')
#
# add_new_list()
#
# print('\nСодержимое словаря после добавления новых записей:')
# for post1, info1 in my_dict.items():
#     print(f'{post1}: {info1}')
#


# def write_list(file_name,list):
#     with open(file_name,"w") as f:
#         for element in list:
#             f.write(f'{element},')
#
# def read_list(file_name):
#     with open(file_name,'r') as f:
#         temp=f.read()
#         list=temp.split(',')
#     return list
#
# list=[8,9,'Привет',6,'Мир']
# write_list('newtext.txt',list)
# read_list_from_file=read_list('newtext.txt')
# print(read_list_from_file)
"""
# def write_list(file_name,list):
#     with open(file_name,'wb') as f:
#         pickle.dump(list,f)
# def read_list(file_name):
#     with open(file_name, 'rb') as f:
#         lst=pickle.load(f)
#     return lst
# list=[8,9,'Привет',6,'Мир']
# write_list('newtext.txt',list)
# read_list_from_file=read_list('newtext.txt')
# print(read_list_from_file)
"""

# def write_list(file_name,list):
#      with open(file_name,mode='wt',encoding='utf8') as f:
#          json.dump(list,f)
#
# def read_list(file_name):
#     with open(file_name, mode='rt',encoding='utf8') as f:
#         lst=json.load(f)
#     return lst
#
# list=[8,9,'Привет',6,'Мир','Hello']
# write_list('newtext.txt',list)
# read_list_from_file=read_list('newtext.txt')
# print(read_list_from_file)


"""# class Bird():
#     def __init__(self,name=' '):
#         self.name=name
#     def sing(self):
#         print(f"My name {self.name}")
#         #print("chik chirik")
#     def _make(self):
#         print("ffff")
# 
#     def __fly(self):
#         print('fly')
# new_bird=Bird()
# new_bird.__init__('gnbwf')
# new_bird.__fly()"""



# input_file_path = "my_list.txt"
# output_file_path = "_mod.txt"
#
# data = []
# try:
#     with open(input_file_path, 'r') as f:
#         for x in f:
#             data.append(float(x))
# except ValueError:
#     print("Ошибка: В файле найдены нечисловые значения")
#     breakpoint()

# mean_value = sum(data) / len(data)
# num = 0
# for x in data:
#     sub = (abs(x - mean_value) ** 2)
#     num += sub
# subtraction = pow(num / len(data), 0.5)
# print(f"СКО:",{subtraction})
#
#
# max_num = data.index(max(data))
# data[max_num] = round(mean_value,10)
#
# def SKO(data):
#     mean_value = sum(data) / len(data)
#     #num = 0
#     i=0
#     # for x in data:
#     #     sub = (abs(x - mean_value) ** 2)
#     #     num += sub
#     # subtraction = pow(num / len(data), 0.5)
#     #print(f"СКО:",{subtraction})
#     for x in data:
#          if x>mean_value:
#              data[i]=mean_value
#          i += 1
#     return data
#     # if subtraction > 3:
#     #     max_num = data.index(max(data))
#     #     data[max_num] = round(mean_value,10)
#     #     SKO(data)
#     #     return data
#     # else:
#     #     return data
# #
# # mean = sum(data) / len(data)
# SKO(data)
#
# with open(output_file_path, 'w') as f:
#     for element in data:
#         f.write(f'{element}\n')
#
# print(f"Исходный файл:\n{open(input_file_path).read()}")
# print(f"Исправленный файл:\n{open(output_file_path).read()}")
#



















#
#
# import numpy as np
#
# def correct_outliers(file_path):
#     with open(file_path, 'r') as file:
#         values = [float(line.strip()) for line in file]
#
#     mean_value = np.mean(values)
#     std_dev = np.std(values)
#
#     outliers = [i for i, value in enumerate(values) if abs(value - mean_value) > 3 * std_dev]
#
#     for outlier_index in outliers:
#         values[outlier_index] = mean_value
#
#     new_file_path = file_path.replace('.txt', '_mod.txt')
#     with open(new_file_path, 'w') as new_file:
#         for value in values:
#             new_file.write(f'{value}\n')
#
#     return new_file_path
#
# input_file_path = "my_list.txt"
# output_file_path = "_mod.txt"
#
#print(f"Исходный файл:\n{open(input_file_path).read()}")
# print(f"Исправленный файл:\n{open(output_file_path).read()}")




lst = [5, 6, [1, 2, 3], 'hfy']


new_lst = []
new_lst.extend('ddd')
print(new_lst)

for item in lst:
    if isinstance(item, list):
        new_lst.extend(item)
    else:
        new_lst.append(item)

print(new_lst)
