# from time import time
# start = time()
# s={}
# def f(n):
#     if n in s:
#         return s[n] -> меморизация
#     if n<2:
#         return n
#     result= f(n-1)+f(n-2)
#     s[n]=result
#     return result
# print(f(100))
# print(time()-start)

# import time
# from functools import lru_cache
# @lru_cache(maxsize=256)
# def fib(n):
#     if n<2:
#         return n
#     return fib(n-1) + fib(n-2)
# start = time.perf_counter()
# print(fib(100))
# end = time.perf_counter()
# print(end - start)
# info=fib.cache_info()
# print(info)

# stack - LIFO - last in first out - пирамида
# очередь - FIFO - first in first out - 0 1 2 3 4 5
# LFU - least frequency used - Библиотека(чаще всего- сохраняются, реже всего- удаляются)
# LRU - least resently used - наименее недавно использованный (ВРЕМЯ)

# import sys
# sys.setrecursionlimit(10**6)
# def f(n):
#     if n < 5:
#         return n
#     return 2*n*f(n-4)
# result=(f(13766)-9*f(13762))//f(13758)
# print(result)

# from functools import lru_cache
# @lru_cache(maxsize=1024)
# def trib(n):
#     if n == 0:
#         return 0
#     if n == 1 or n == 2:
#         return 1
#     return trib(n-1) + trib(n-2) + trib(n-3)
# print(trib(3))

# from functools import lru_cache
# @lru_cache(maxsize=None)
# def count_ways(n):
#     if n == 0:
#         return 1
#     if n==1:
#         return 1
#     return count_ways(n-1)+count_ways(n-2)
# print(count_ways(5))