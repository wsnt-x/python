# for n in range(1,200):
#     b=bin(n)[2:]
#     if n%2==0:
#         b=b+"00"
#     else:
#         b=b+"11"
#     r=int(b,2)
#     if r>115:
#         print(n)



# for n in range(1,200):
#     b=bin(n)[2:]
#     if n%2!=0:
#         b="1"+b+'11'
#     else:
#         b="11"+b+"00"
#     r=int(b,2)
#     if r<127:
#         print(r)


# for n in range(1,200):
#     b=bin(n)[2:]
#     if b.count('1')%2==0:
#         b=b+'10'+b[2:]+'0'
#     else:
#         b="11"+b[2:]+"1"
#     r=int(b,2)
#     if r<35:
#         print(r)

# a=[]
# for n in range(1, 100):
#     b=bin(n)[2:]
#     if n%2==0:
#         b="10"+b
#     else:
#         b="1"+b+"01"
#     r=int(b,2)
#     if n>18:
#         a.append(r)
# print(min(a))

# a=[]
# for n in range(2000):
#     b=bin(n)[2:]
#     if n%7==0:
#         b=b+"01"
#     else:
#         q=bin(n//7)[2:]
#         b=b+q
#     r=int(b,2)
#     if n%2!=0 and r<=1300:
#         a.append(n)
# print(max(a))

# a=[]
# def s12(n):
#     s=""
#     while n>0:
#         s=str(n%12)+s
#         n=n//12
#     return s
# for n in range(11,1000):
#     b=s12(n)
#     if n%12==0:
#         b=b+b[-2:]
#     else:
#         b=b+s12(n%12*9)
#     r=int(b,12)
#     if r>300:
#         a.append(r)
# print(min(a))


# def s3(n):
#     s=""
#     while n>0:
#         s=str(n%3)+s
#         n=n//3
#     return s
# for n in range(1000):
#     b=s3(n)
#     if n%2==0:
#         b="1"+b+"00"
#     else:
#         b = b + s3(sum(map(int, s3(n))))

# a=[]
# def s3(n):
#     if n==0:
#         return "0"
#     s=""
#     while n>0:
#         s=str(n%3)+s
#         n=n//3
#     return s
# for x in range(1,1000):
#     b=s3(x)
#     if x%3==0:
#         b=b+b[-2:]
#     else:
#         b=b+s3(((x%3)-1)*3)
#     r=int(b,3)
#     if r<=200:
#         a.append(r)
# print(max(a))



# ИЗ 10 В 2
# x10=55
# x2=f"{x10:b}"


# for n in range(1000,1,-1):
#     n2=f"{n:b}"
#     if n%2==0:
#         n2="10"+n2
#     else:
#         n2="1"+n2+"01"
#     r=int(n2,2)
#     if r<30:
#         print(n)
#         break

# ans=[]
# for n in range(1,10000):
#     n2=f"{n:b}"
#     n2=n2+str(n2.count('1')%2)
#     n2=n2+str(n2.count('1')%2)
#     r=int(n2,2)
#     if r>75:
#             ans+=[r]
# print(min(ans))

# ИЗ 10 В 3
# def per3(x):
#     if x == 0:
#         return "0"
#     s = ""
#     while x > 0:
#         s = str(x % 3) + s
#         x = x // 3
#     return s

# ИЗ 10 В ЛЮБУЮ ДО 10
# def per(x, osn):
#     if x == 0:
#         return "0"
#     s = ""
#     while x > 0:
#         s = str(x % osn) + s
#         x //= osn
#     return s


# s[start:stop:step]
# start — откуда начинаем (включительно)
# stop — где заканчиваем (НЕ включая)
# step — шаг
# s[a:b]    # от a до b
# s[:b]     # с начала
# s[a:]     # до конца
# s[:]      # копия
# s[::-1]   # разворот
# s[::2]    # каждый второй