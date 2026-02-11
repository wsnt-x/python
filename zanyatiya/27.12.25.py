# Реализуйте метод find(). На вход поступают строка st и
# подстрока substring (вводятся пользователем).
# Необходимо найти индекс первого вхождения substring
# в st. Если подстрока не найдена, вернуть -1.
# Входные данные:
# hello world python
# world
#
# Выходные данные:
# 6

# def find(st:str, substring:str):
#
#     for i in range(len(st)):
#         #helli world
#         #hello
#         flag = True
#         for j in range(len(substring)):
#             if st[i + j] != substring[j]:
#                 flag = False
#                 break
#         if flag:
#             return i
#     return -1
#
# find(input(), input())

# Реализуйте метод reverse() для списка.
# На вход поступает список lst (вводится пользователем).
# Необходимо развернуть список (изменить порядок элементов на
# обратный) и вывести результат. Реализовать при помощи цикла
# for или while на ваше усмотрение, без использования срезов [::-1]
# Входные данные:
# 1 2 3 4 5
# Выходные данные:
# [5, 4, 3, 2, 1]

# a = [1,2,3,4]
# print(a[len(a)-1])
# print(a[-2])

# remove()
# pop()


# def reverse(a):
#     b = []
    # for i in range(len(a)-1,-1,-1):
    #     b.append(a[i])
    # for i in range(len(a)):
    #     b.append(a[-i-1])
    # return b
# a = list(map(int,input().split()))
# print(reverse(a))

# Реализуйте метод index().
# На вход поступают список lst и элемент element
# (вводятся пользователем).
# Необходимо найти индекс первого вхождения элемента
# element в списке lst. Если элемент не найден,
# вывести сообщение "Элемент не найден в списке".
# Входные данные:
# 10, 20, 30, 40, 50, 30, 60
# 30
# 10, 20, 30, 40, 50, 30, 60
# 0
# Выходные данные:
# Индекс элемента 30: 2
# Элемент не найден в списке


# def a(lst,el):
#     for i in range(len(lst)):
#         if lst[i] == el:
#             return i
#     return "Эл-т не найден"
#
# lst = [10,20,30,40,50]
# el = 50
# flag = False
# for i in range(len(lst)):
#     if lst[i] == el:
#         flag = True
#         print(i)
# if el not in lst or not flag:
#     print("Эл не найден")
# print(a(lst,el))

# Напишите функцию для частотного анализа слов в строке.
# пользователь вводит
# 1 Функция должна принимать строку
# 2 разделить строку
# 3 привести слова к нижнему регистру
# 4 слеоать слова уникальными (опцинально)
# 5 считаем количество совпадений
# 6 соединить строку в словрь ключь - значение - количество
# возвращать словарь в котором
# ключами являются все уникальные слова этой строки (функция должна
# быть нечувствительна к регистру), а значениями — количество
# повторений каждого слова в строке.
# Необходимо написать свой алгоритм в функции, без использования модулей.
# Аргумент функции необходимо считать с пользовательского
# ввода и передать в функцию.
# Входные данные:
# aa ab abab baba aa ba
# Выходные данные:
# {'aa': 2, 'ab': 1, 'abab': 1, 'baba': 1, 'ba': 1}

# def func(string):
#     string = string.lower()
#     lst_string = string.split()
#     set_lst_string = set(lst_string)
#     s = {}
#     for item in set_lst_string:
#         s[item] = lst_string.count(item)
#     return s
# print(func(input()))
#
# #d - десятичная
# print(f"{27:d}") #десятичная система счисления int
# #b - двоичная bin
# print(f"{27:b}")
# #o - восмеричная oct
# print(f"{27:o}")
# #x - шеснадцатиричная hex
# print(f"{27:x}")
#
# a = 1.2362332432
# print(f"fklsdfklsdkflskdl;f{a:.2f}")

# import string
# print(string.printable)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
# print(string.whitespace)

# Дан список задач с процентом выполнения.
# Выведите список с прогресс-барами из символов '=' и '>'.
# Ожидаемый вывод:
#
# Прогресс задач:
# Задача 1: [==========] 100%
# Задача 2: [====>     ] 50%
# Задача 3: [          ] 0%

# tasks = [
#     {"name": "Задача 1", "progress": 100},
#     {"name": "Задача 2", "progress": 50},
#     {"name": "Задача 3", "progress": 0}
# ]