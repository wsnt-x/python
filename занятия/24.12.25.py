#startwith()
# s="hello"
# b="h"
# print(s.startswith(b))


# def f(s1:str,s2:str):
#     if s1<s2:
#         return False
#     else:
#         for i in range(len(s2)):
#             if s2[i]!=s1[i]:
#                 return False
#     return True
# print(f("hello","qwe"))


# s="hello world hello python hello".split()
# subs=input()
# k=0
# for i in s:
#     if subs==i:
#         k+=1
# print(k)


# def count(st, substring):
#     k = 0
#     if st < substring:
#         return False
#     else:
#         for i in range(len(st)):
#             flag = False
#             for j in range(len(substring)):
#                 if st[i + j] != substring[j]:
#                     flag = True
#                     break
#             if not flag:
#                 k += 1
#     return k
# print(count('hello world hello world', 'hello'))










# def replace(st, old, new):
#     string = ''
#     if old not in st:
#         return False
#     else:
#         for i in range(len(st)):
#             flag = False
#             for j in range(len(old)):
#                 if st[i + j] != old[j]:
#                     flag = True
#                     break
#             if not flag:
#                 string += new
#                 i += len(old)
#             else:
#                 string += st[i]
#                 i += 1
#     return string
# print(replace('hello world hello python', 'hello', 'hi'))