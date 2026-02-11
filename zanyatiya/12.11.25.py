# a=(1,2,3,4,5)#кортеж tuple
# b=[1,2,3,4,5]
# print(tuple(b))#перевод типов
#
# s="23"
# # a[1]=0
# print(s[0])
#
# DENNIM="hello world"
# s=("hello","world")
#
# coords=(100,300)
#
# values=(1,2,3,4,5)
# x=1
# y=2
# x,y=y,x
# s1,*s2,s3,s4=values
# print(s1,s2,s3,s4)
#
# s=(1,2,3)
# s1=(4,5)
# print(*s,*s1)
# s3=(*s,*s1)
# print(s3)
#
# next_tuple=(1,(2,3,4),5)
# s1,(s2,*s4),s3=next_tuple
# print(s4)
# # print(*next_tuple[1][1:])
#
# s=((1,2),(3,4),(5,6))
# for i in s:
#     print(i[0], "+",i[1],"=",i[0]+i[1])

# for i,j in s:#подчиняется правилам распаковки
    # print(i,"+",j,"=",i+j)

# next=[([1,2],3),["XY",6]]
# for ((i,b),j) in next:
#     print(i,b,j)

#set
# a={1,2,3,4,5,6,1,2,3,4,5}
# b=[1,2,3,5]
# print(set(b))
# print(a)

# s={(1,2),(3,4)}
# # s={[1,2],[3,4]} error
# print(s)
#
# s.add((5,6))# добавление элемента во множество
# print(s)
# s.remove((1,2))#удаление элемента множества
# print(s)



#34
# a=(1,2,3)
# s1,s2,s3=a
# print(s1)
# print(s2)
# print(s3)

#40
# a=input().split()
# for i in range(len(a)):
#     a[i]=float(a[i])
# a=tuple(a)
# *s,s1=a
# #reverse
#reversed .reverse list
# #s=reversed(s)
# print(s[::-1],s1)


#42
# a=(1,2,3)
# b=(4,5,6)
# c=()
# for i in range(len(a)):
#     i=a[i]+b[i]
#     # c=(*c,i)
#     c+=(i,)#обязательно нужно ставить запитую, чтобы было понятно, что это кортеж
# print(c)

# set_1={1,2,3,4,5,6}
# set_2={4,5,6,7,8,9}
# set_3=set_1.union(set_2)#объединение
# set_4=set_1.update(set_2)
# print(set_3)

# set_3=set_1.intersection(set_2)#пересечение
# set_1.intersection_update(set_2)

# set_3=set_1.difference(set_2)#разность
# print(set_3)
# set_3=set_1.symmetric_difference(set_2)#симметричная разность
# print(set_3)

# set_1={1,2,3}
# set_2={4,1,2,3,8,9}
# print(set_2.issubset(set_1))
# print(set_1.issubset(set_2))#входит ли в подмножество
# print(set_2.issuperset(set_1))
# print(set_1.issuperset(set_2))#ф-ция обратная от подмножеств


#57
a=input()
b=set(a)
print(b,len(b))
if len(b)<len(a):
    print("Есть")
else:
    print("Нет")