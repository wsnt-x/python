# # аргументы принимаемые функцией
# def name_func(first_arg,*, second_arg=15):# функция
#     # *- ограничение которое ожидает обращения
#     # тело функции
#     for i in range(first_arg, second_arg):
#         print(i)
#         # конец тела функции
#
# #параметры
# # name_func(second_arg=25) # вызов функции
# name_func(10,25)

#названия функций уникальны (строятся как и переменные)
# / - без наименований в параметрах
# def name_func_2(x,y,/):
#     print(x,y)
#     pass # ничего (заглушка)
# name_func_2(10,25)#можно

# def name_func_3(*args):
#     for i in args:
#         print(i)
# name_func_3(1,2,"alsasd",4,5,6)

# # **kwargs - словарь
# def name_func_4(**kwargs):
#     kwargs.pop("name2")
#     # print(kwargs['name1'])
#     print(kwargs)
# name_func_4(name1 = 1, name2 = 2)

# def a():
#     d=[[[1,2,3],[4,5,6],[7,8,9]]]
#     def b(x,y,z):
#         for i in range(x):
#             for j in range(y):
#                 for k in range(z):
#                     print(d[i][j][k])
#     b(len(d),len(d[0]),len(d[0][0]))
# a()

# x=20# глобальная область видимости
# def local_func():
#     # global x
#     x=10 # локальная область видимости
#     print(x)
#
#     return x,x,x # возвращаем значение
# print(local_func()[0]+25)
# print(x)

# def a():
#     x=10 #охватывающая область
#     def b():
#         nonlocal x
#         x=5
#         print(x)
#     b()
#     print(x)
# a()

# def square(x):
#     while True:
#         while True:
#             if x==5:
#                 return
#             x+=1
# print(square(5))

# x:int=0
# def func(s:str) ->list:
#     """
#     эта функция делает чтото
#     :return:
#     ничего
#     """
#     global x
#     while True:
#         while True:
#             if x>=5:
#                 return [1,2,3]
#             x+=1
# print(func("hello"))
# print(x)

# #Задача 2
# def func(x:int,y:int): #аннотация типов
#     """
#
#     :param x:
#     :param y:
#     :return:
#     """
#     #type(x)==int -> isinstance(x,int)
#     if type(x)==int and type(y)==int and y!=0:
#         return x/y
#     return "error"
# print(func(4,3))

# #Задача 3
# def is_even(n:int):
#     return n % 2 == 0
# print(is_even(6))
