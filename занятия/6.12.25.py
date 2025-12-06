# import string
# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.punctuation)
#
# print("hello"+":"+"world")
# a=":"
# print(f"hello{a}world{a}{a}")

#4
# from random import *
# import string
# a=[]
# for i in range(100):
#     f=choice(string.ascii_uppercase)
#     g=randint(0,9)
#     a.append(f"{f}{g}\n")
# with open("hw6.txt","w") as f:
#     f.writelines(a)
# with open("hw6.txt","r") as f:
#     for i in f:
#         a=f.readline()
#         if int(i[1])%2==0 and i[1]!="0":
#             print(i)
#             break
#

#5
# with open("hw6.txt","r") as f:
#     # count=0
#     # for line in f:
#     #     if line[0]=="A":
#     #         count+=1
#     # print(count)
#     #ЛУЧШЕ
#     a=":".join(f.readlines()).count("A")
#     print(a)

#8
# import string
# from random import randint,choice
# with open("7.txt","w+") as f:
#     for i in range(150):
#         a=randint(0,9)
#         b=choice(string.ascii_uppercase)
#         f.write(f"{a}-{b}\n")
# with open("7.txt","r") as f:
#     for i in f:
#         f.readline()
#         if int(i[0])>5:
#             print(i)

#9
with open("903.txt", "r") as f:
    for line in f:
        numbers=line.split("\t")
        maxim=0
        minim=9999999
        for i in numbers:
            if int(i)>maxim:
                maxim=int(i)
            if int(i)<minim:
                minim=int(i)



