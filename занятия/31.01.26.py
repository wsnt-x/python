# def recursion(num):
#
#     return recursion(num*2)

# school=[
#     [
#         ["a","b","c"],["a","b","c"],["a","b","c"],["a","b","c"]
#     ],
#     [
#         ["a","b","c"],["a","b","c"],["a","b","c"],["a","b","c"]
#     ]
# ]
# k=0
# for school_item in school:
#     for class_item in school_item:
#         for sym in class_item:
#             k+=1
#             print(sym)
# print(k)

# summ=0
# def school_ref(school):
#     global summ
#     if len(school)==1:
#         summ+=1
#         return
#     for i in school:
#         return school_ref(i)
# print(school_ref(school),summ)

# def rec(b):
#     # if type(b)==int:
#     #     return b +
#     if b==1:
#         return 1
#     return b+rec(b-1)
# g=rec(10)
# print(g)

# a=[1,2,3,4,5,6,7,8]
# def rec(lst):
#     if not lst:
#         return 0
#     return lst[0]+rec(lst[1:])
# print(rec(a))

# def reverse_str(s):
#     result=""
#     for char in s:
#         result=char+result
#     return result
# def reverse_rec(s):
#     if len(s)<=1:
#         return s
#     return reverse_rec(s[1:])+s[0]
# print(reverse_rec("hello"))

# факториал рекурсивно
# факториал обычно

# измерить время выполнения
from time import time
# start=time()
# def f(n):
#     if n==1:
#         return 1
#     return n*f(n-1)
# g=f(30)
# print(g)
# print(time()-start)

# def just(a):
#     mult=1
#     for i in range(1,a+1):
#         mult*=i
#     return mult
# print(just(5))

# import sys
# sys.setrecursionlimit(999999)
# start=time()
# def just(n):
#     if n==1:
#         return 1
#     return just(n-1)*n
# just(32755)
# print(time()-start)

# LIFO - first in last out
# [ 6 7 ]
# def A():
#     B()
# def B():
#     C()
# def C():
#     pass
# A()
# Pop - удаление и возвращение первого эл-та
# Push - добавление нового элемента в стек

# from time import time
# start=time()
# def fib(n):
#     if n<2:
#         return n
#     return fib(n-2)+fib(n-1)
# print(fib(35))
# print(time()-start)