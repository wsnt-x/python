#11
# def analyze_text(text):
#     sentences=text.count(".")+text.count("!")+text.count("?")
#     words=len(text.split())
#     symbols=len(text)
#     return (sentences,words,symbols)
# print(analyze_text("Hello World. Zsdasdasd! Dafasda?"))

#21
# import math
# def calculate_area(shape="rectangle",length=0,width=0,radius=0):
#     if shape=="rectangle":
#         return length*width
#     elif shape=="circle":
#         return math.pi*(radius*radius)
# print(calculate_area("circle",12,2,2))

#25
# def format_name(first:str,last:str,middle:str="",title=""):
#     return title+" "+first+" "+last+" "+middle
# print(format_name("John","Smith",title="mr"))

#23
# def a(*args): #после звездочки
#     return list(set(args))
# print(a(1,2,3,3,4,5,6,7,8,9))

#29
# from random import randint
# def f_nums(a: int, b:int):
#     list_nums = []
#     for _ in range(a,b):
#         z = randint(0,100)
#         list_nums.append(z)
#     maxim = 0
#     digit = -1
#     for i in list_nums:
#         value_cash = list_nums.count(i)
#         if maxim < value_cash:
#             digit = i
#             maxim = value_cash
#     return list_nums, digit, maxim
# print(f_nums(1,50))

# def a(g):
#     print(g)
#     g.append (10)
# g = [1,2,3]
# a (g. copy ())
# print(g)