# 1. Напишите рекурсивную функцию для вычисления a^n (a в степени n).
# def rec(a,n):
#     if n==0:
#         return 1
#     return a*rec(a,n-1)
# print(rec(3,4))
# 2. Напишите рекурсивную функцию для нахождения суммы цифр числа.
# def f(n):
#     if n == 0:
#         return 0
#     return n%10+f(n//10)
# print(f(123))
# 3. Напишите рекурсивную функцию для нахождения максимального элемента в списке.
# def recursion(lst:list): # [ 1 2 3 4 ]
#     if len(lst) == 1:
#         return lst[0]
#     return lst[0] if lst[0] > recursion(lst[1:]) else recursion(lst[1:])
# print(recursion([1,2,10,1]))
