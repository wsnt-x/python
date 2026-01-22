# k=0
# for a in "ГЕПРД":
#     for b in "ГЕПАРД":
#         for c in "ГЕПАРД":
#             for d in "ГЕПАРД":
#                 for e in "ГПАРД":
#                     s=a+b+c+d+e
#                     if s.count("Г")==1:
#                         k+=1
# print(k)

# from itertools import *
# k=0
# for i in permutations("ЛЕВИОСА"):
#     s="".join(i)
#     if s[0] not in "ЕИОА" and s[3] not in "ЛВС":
#         k+=1
# print(k)

# from itertools import *
# k=0
# for i in set(permutations("АБИКОЛУН")):
#     s="".join(i)
#     s=s.replace("И","А").replace("О","А").replace("У","А")
#     s=s.replace("К","Б").replace("Л","Б").replace("Н","Б")
#     if "АА" not in s and "ББ" not in s:
#         k+=1
# print(k)

# k=0
# for a in ("2468"):
#     for b in ("012345678"):
#         for c in ("012345678"):
#             for d in ("012345678"):
#                 for e in ("012345678"):
#                     for f in ("012345678"):
#                         for h in ("1357"):
#                             s=a+b+c+d+e+f+h
#                             if s.count("8") == 1:
#                                 k+=1
# print(k)


# def f(n):
#     for i in range(len(n) - 1):
#         if (int(n[i]) + int(n[i + 1])) % 2 == 0:
#             return False
#     return True
# nums = list('0123456')
# count = 0
# for a1 in nums[1:]:
#     for a2 in nums:
#         for a3 in nums:
#             for a4 in nums:
#                 for a5 in nums:
#                     for a6 in nums:
#                         a = a1 + a2 + a3 + a4 + a5 + a6
#                         if f(a) and a.count ('6') == 1:
#                             count += 1
# print(count)

from itertools import *
k=0
for x in permutations("АПЕЛЬСИН",r=7):
    s="".join(x)
    for y in "ПЛСН": s=s.replace(y,"С")
    if ("Ь" not in s) or ("СЬС" in s):
        k+=1
print(k)
