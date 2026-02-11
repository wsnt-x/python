# t=(5,5,5,3,4,5,5,4,4,4,4,4)
# counter=1
# maxim=0
# for i in range(1,len(t)):
#     if t[i-1]==t[i]:
#         counter+=1
#     else:
#         if maxim<counter:
#             maxim=counter
#         counter=1
# print(maxim)


#47
# cart=[("яблоки",100),("хлеб",50),("молоко",80),("яблоки",100)]
# cart.pop(3)
# for i in range(len(cart)):
#     if cart[i][1]>70:
#         print(cart[i][0])
# a=[200,50,160]
# print(a)
# cart1=[]
# for i in range(3):
#     cart1.append(cart[i][0])
#     cart1.append((cart[i][1])/2)
# print(cart1)

#ЛУЧШЕ:
# cart=[("яблоки",100),("хлеб",50),("молоко",80),("яблоки",100)]
# cart1=[]
# cart2=[]
# cart3=[]
# for i,j in cart:
#     if j>70:
#         cart1.append((i,j))
# print(cart1)
# for i,j in cart:
#     cart2.append((i,j*2))
# print(cart2)
# for i,j in set(cart):
#     cart3.append((i,j/2))
# print(cart3)

#48
# books = [("Война и мир", 1865), ("1984", 1949), ("Гарри Поттер", 1997), ("Война и мир", 1865)]
# books1=[]
# books2=[]
# books3=[]
# for i,j in books:
#     if j>1900:
#         books1.append((i,j))
# print(books1)
# for i,j in books:
#     books2.append((j-100))
# print(books2)
# for i,j in books:
#     if j<1950:
#         books3.append(("Классика:",i,j))
#     else:
#         books3.append((i,j))
# print(books3)

#59
# math_students = {"Анна", "Борис", "Вера", "Глеб"}
# physics_students = {"Борис", "Вера", "Дмитрий", "Елена"}
# chemistry_students = {"Вера", "Глеб", "Дмитрий", "Жанна"}
# print(math_students.intersection(physics_students).intersection(chemistry_students))
# # print(math_students&physics_students&chemistry_students) #тоже самое что и intersection
# print(math_students.difference(physics_students,chemistry_students))#difference
# # print(math_students-physics_students-chemistry_students)#difference
# print(math_students.union(physics_students)-chemistry_students)#union
# #print((math_students | physics_students) - chemistry_students)#union

#62
a=[]
for i in range(20):
    if i%2==0:
        a.append(i)
print(set(a))
b=[]
for i in range(30):
    if i%3==0:
        b.append(i)
print(set(b))
print(set(a)&set(b))
c=[]
for i in range(1,20):
    if i%2==0 and i%3==0:
        c.append(i)
print(c)



