# from itertools import *
#
# def f(x,y,z,w):
#     return (not(x<=z)) or (y==w) or y
#
# for a1,a2,a3,a4,a5,a6,a7 in product([0,1],repeat=7):
#     t=[(1,0,a1,a2),
#        (a3,1,0,a4),
#        (0,a5,a6,a7)]
#     if len(t)==len(set(t)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p,r))) for r in t] == [0,0,0]:
#                 print(*p)

# a = []
# for n in range(1, 1000):
#     b = f'{n:b}'
#     b = b + str(b.count('1') % 2)
#     b = b + str(b.count('1') % 2)
#     r=int(b,2)
#     if r>396:
#         a.append(r)
# print(min(a))

# from turtle import *
#
# tracer(0)
# screensize(10000,10000)
# lt(90)
# r=10
#
# for i in range(8):
#     fd(16*r)
#     rt(90)
#     fd(22*r)
#     rt(90)
# up()
# fd(5*r)
# rt(90)
# fd(5*r)
# lt(90)
# down()
# for i in range(8):
#     fd(52*r)
#     rt(90)
#     fd(77*r)
#     rt(90)
#
# for x in range(5,23):
#     for y in range(5,17):
#         teleport(x*r,y*r)
#         dot(3,'red')
#
# print(11*17)
# print((23-5-1)*(17-5-1))
# update()
# done()

# from itertools import *
# k=0
# for i in product('ГЕПАРД',repeat=5):
#     s=''.join(i)
#     if s.count('Г')==1 and s[0]!='А'and s[-1]!="Е":
#         k+=1
# print(k)

# k=0
# with open('9.txt') as f:
#     for i in f:
#         k+=1
#         a=sorted(list(map(int,i.split())))
#         if len(a)==len(set(a)):
#             if 2*(a[0]+a[1]+a[2])<(a[3]+a[4]+a[5]):
#                 print(k)

# from ipaddress import *
#
# nn=ip_network('122.159.136.144/255.255.255.248',0)
# k=0
# for ip in nn:
#     b=f'{ip:b}'
#     if b.count('1')%4!=0:
#         k+=1
# print(k)

# from math import *
#
# a=10+2030
# i=ceil(log2(a))
# for l in range(1,1000):
#     idn=ceil(i*l/8)
#     if idn*318>67*2**10:
#         print(l)
#         break

# def f(z):
#     s=[]
#     while z>0:
#         s.append(z%11)
#         z//=11
#     return s[::-1]
# for x in range(1,3001):
#     a=9*11**210+8*11**150-x
#     if f(a).count(0)==60:
#         print(x)


# b=list(range(36,76))
# c=list(range(60,111))
# a=list()
# for x in range(1000):
#     if not ((x not in a) <= ((x in b)==(x in c))):
#         a.append(x)
# print(a)
# print(len(a))
# print(a[-1]-a[0])

# k=0
# sumi=0
# with open('17.txt') as f:
#     a=[int(i[:-1]) for i in f.readlines()]
#     b=[]
#     for i in range(len(a)-2):
#         b.append([a[i],a[i+1],a[i+2]])
#     maxi=max([x for x in a if x%100==25])
#     for i in b:
#         znach=[x for x in i if x in list(range(1000,10000))]
#         sumz=sum(i)
#         if len(znach)<=2:
#             if sumz <= maxi:
#                 k+=1
#                 sumi=max(sumi,sumz)
# print(k,sumi)