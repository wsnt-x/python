# count / find / rfind / (is)lower / (is)upper /
# set / bool / int / str / tuple / list / float / dict / None
#sort / sorted
# reversed
# "hello" "A" replace()
# isAlpha...betta
# type
from os import PRIO_PGRP

# if elif elsse

# match case

# for while

# def name()

#1
# a=input().split()
# for i in a:
#     print(i[::-1],end='')


# all() and
# any() or

# print(any([True, True, False])) # эквивалент and
# print(all([True, True, False])) # эквивалент or

# a=[]
# for i in range(1,10):
#     a.append(i%10==0)
# print(a)
# print(any(a))
# print(all(a))

#2
# a=[10,20,30,40,50]
# print(all(i>=0 for i in a))

#3
# a=["","hello","","world"]
# print(any(i!="" for i in a))

#enumerate(последовательность, начальный индекс = 0)
# a=["h","e","l","l"]
# print(list(enumerate(a, start=0)))
# for i in range(len(a)):
#     print(a[i])
#
# for i,item in enumerate(a,start=0):
#     print(i,item)

# my_dict={"k1":"z1","k2":"z2","k3":"z3"}
#
# for key,value in my_dict.items():
#     print(key,value)
# for i, (k, v) in enumerate(my_dict.items(),start=0):
#     print(i,k,v)

# *
# a=((1,2,3,4,5),(6,7,8,9,10),)
# (z,*y),(k,*s)=a # пакуем элементы
# print(k,s)
# print(z,y)
# print(*a[0],sep="")

#2
# a=[10,25,30,15,40,5,50]
# for i,item in enumerate(a):
#     if item>20:
#         print(i,item)

#3
# a=["python","java","c","javascript","go","rust","php"]
# for i,item in enumerate(a):
#     if "a" in item and  len(item)>3:
#         print(i,item)


# a=["hello","my name is"]
# b=["world","max","lesson"]
# # for first,second in zip(a,b):
# #     print(first,second)
# print(list(zip(a,b)))

# pairs=[(1,"a"),(2,"b"),(3,"c"),(4,"d")]
# nums,letters=zip(*pairs)
# print(nums)
# print(letters)

# names=["Алексей","Мария","Иван"]
# ages=[25,30,22]
# for a,b in zip(names,ages):
#     print(f"{a} : {b} лет")

# students = ['Анна', 'Борис', 'Виктор']
# subjects = ['Математика', 'Физика', 'Химия']
# grades = [5, 4, 5]
# for student, subject, grade in zip(students, subjects, grades):
#     print(f"{student}-{subject}-{grade}")


# prices=[100,200,150,300]
# discounts=[10,15,5,20]
# for a,b in zip(prices,discounts):
#     print(a-(a*(b/100)))

