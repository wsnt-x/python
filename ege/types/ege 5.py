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

