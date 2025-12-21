# егэ 14
# перевод из 10 сс
# def f(n):
#     a=[] #список цифр числа в новой сс
#     while n>0: #пока в числе есть разряды
#         a.append(n%9) #сохраняем последнюю цифру
#         n=n//9 #переводим в сс нужным основанием
#     return a[::-1] #возвращаем результат перевода
# n27=f(234242342423)
# print(n27.count(5)-n27.count(0))

# c неизвестным x
# def f(n):
#     a=[]
#     while n>0:
#         a.append(n%9)
#         n=n//9
#     return a[::-1]
# for x in range(1,99999):
#     n9=f(9**1942+9*6**971+214-x)
#     if n9.count(8)-n9.count(2)==471:
#         print(x)
#         break



# def f(n):
#     a=[]
#     while n>0:
#         a.append(n%5)
#         n=n//5
#     return a[::-1]
# m=[]
# for x in range(2,2026):
#     n7=f(5**2025+5**200-x)
#     #теперь уже зная что макс нулей = 73
#     #я могу найти при каких x это возможно
#     if n7.count(4)==199:
#         print(x)
# #     m.append(n7.count(4))
# # print(max(m))

#
#
# for N in range(2, 200):
#     if 41 % N == 2 and 131 % N == 1:
#         print("Подходит основание системы счисления N =", N)
#



# result = []
#
# for N in range(1, 500):
#     # условие 1: две цифры в системе счисления с основанием 6
#     if not (6 <= N < 36):
#         continue
#
#     # условие 2: три цифры в системе счисления с основанием 5
#     if not (25 <= N < 125):
#         continue
#
#     # условие 3: запись в системе 11 оканчивается на 1
#     if N % 11 != 1:
#         continue
#
#     result.append(N)
#
# print(result)


# count = 0
# for N in range(125, 243):  # включительно: 125..242
#     if N % 16 == 13:
#         count += 1
#
# print(count)


# в 10 сс

# int(n,b)# переводит число n из сс с основанием b в сс с основанием 10
# она работает только для сс от 2 до 36 включительно

# from string import *
# for x in printable[:37]:
#     n=int(f"98{x}31",37)+int(f"1{x}924",37)
#     if n%21==0:
#         print(x,n//21)


# n1 = 'C59xBA98F'
# n2 = 'E3x5DA9C6'
#
# s1 = sum(int(z, 36) for z in n1)
# s2 = sum(int(z, 36) for z in n2)
#
# for x in range(36, -1, -1):
#     if (s1 + x) * (s2 + x) % 36 == 0:
#         print(2 * 37**2 + x * 37 + 1)
#         break

# from string import *
# for x in printable[:37]:
#     for y in printable[:37]:
#         n=int(f"12{y}{x}9",37)+int(f"36{y}99",37)
#         if n%18==0:
#             print(x,y,n//18)


