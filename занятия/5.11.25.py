# a=[1,2,3]
# iterator=iter(a)
# print(next(interator))
# print(next(interator))
# # print(next(interator))
# k=[1,2,3]
# for i in range(0,len(k)):
#     k[i]+=1
# print(k)

# k=[1,2,3]
# l=[4,5,6]
# # z=k+l
# k.extend(l)#расширяет один объект другим
# print(k)


# from random import randint
# k=[]
# for i in range(5):
#     #добавляет новый элемент в конец списка
#     k.append(randint(1,100))
# print(k)

# k=["раз","три"]
# j=["Два"]
# k.insert(1,j[0])# вставляет перед необходимым индексом значение
# print(k)


# k=[1,2,3,4,2,5]
# k.remove(2)#удаляет первый найденный эл-т
# print(k)

# k=[1,2,3,4,2,5]
# k.clear()#чистит список
# print(k)

# k=[1,2,3,4,2,5]
# k.pop(4)#удаляет эл-т по индексу
# print(k)

# k=[5,4,3,2,1,2,3,4,5]
# k=["c","a","b","d","e","f"]
# k.sort(reverse=False)#reverse=False//True - в каком порядке сортировка в обычном или в обратном
# print(k)


# k=[1,2,3,4,5]
# k.reverse()#перевораивает список
# print(k)

# k=[1,2,3,4,5]
# print(max(k))
# print(min(k))
# print(sum(k))

#1
# a=[1,2,3,4,5]
# for i in range(0,len(a)):
#     a[i]*=2
# print(a)
#4
# a=[1,2,3,4,10]
# iterator=iter(a)
# summury=0
# for _ in range (len(a)):
#     summury+=next(iterator)
# print(summury)


# a=[1,2,3,4,5]
# b=[6,7,8,9,10]
# for i in range(len(a)):
#     a[i]=a[i]+b[i]
# print(a)

#8
# a=["av","bas","cslk"]
# for x in a:
#     count=0
#     for _ in x:
#         count+=1
#     if count%2==0:
#         print(x)
#11
#1
# from random import randint
# a="Разряд"
# b=randint(1,100000)
# b=str(b)
# count=0
# for i in b:
#     count+=1
# print(a*count)
#2
from random import randint
for _ in str(randint(0,100000)): print("Разряд")