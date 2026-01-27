# with open("9 1.txt","r") as f:
#     k=0
#     for line in f:
#         a=sorted([int(x) for x in line.split()])
#         if (a[0]+a[2])/2<=a[1]:
#             k=k+1
#             print(k)
# with open("9 1.txt") as f:
#     k = 0
#     for line in f:
#         a = sorted(map(int, line.split()))
#         cond2 = False
#         for x in a:
#             if a.count(x) == 3 and len(set(a)) == 4:
#                 cond2 = True
#         cond1 = (a[0] + a[5]) ** 2 > sum(x * x for x in a[1:5])
#         if cond1 or cond2:
#             k += 1
# print(k)


# with open("9 1.txt","r") as f:
#     k=0
#     for line in f:
#         a=sorted(map(int,line.split()))
#         summ = 0
#         isFirst = False
#         pov = 0
#         for x in a:
#             if a.count(x) == 3 and len(set(a)) == 5:
#                 pov = x
#                 isFirst = True
#             if a.count(x) < 3:
#                 summ += x
#         isSecond = (summ / 4) <= pov
#         if isFirst and isSecond:
#             k += 1
# print(k)

# with open("9 1.txt", "r") as f:
#     k=0
#     for line in f:
#         a=sorted(map(int, line.split()))
#         if len(set(a))==5 and 2*(a[0]+a[4])<=3*(a[1]+a[2]+a[3]):
#             k+=1
#         print(k)


# В каждой строке электронной таблицы записаны шесть целых чисел.
# Определите, сколько в таблице строк, для которых выполнены следующие условия:
#
# в строке есть как повторяющиеся, так и неповторяющиеся числа;
#
# среднее арифметическое всех неповторяющихся чисел строки меньше, чем среднее арифметическое всех повторяющихся чисел этой строки.
#
# При вычислении средних значений каждое число учитывается столько раз, сколько оно встречается в строке.
# В ответе запишите число — количество строк, для которых выполнены эти условия.
#
# with open("9 1.txt") as f:
#     k = 0
#     for line in f:
#         a = list(map(int, line.split()))
#         rep = []  # повторяющиеся числа
#         uniq = []  # неповторяющиеся числа
#         for x in a:
#             if a.count(x) > 1:
#                 rep.append(x)
#             else:
#                 uniq.append(x)
#         # в строке должны быть И повторяющиеся, И неповторяющиеся
#         if len(rep) > 0 and len(uniq) > 0:
#             if sum(uniq) / len(uniq) < sum(rep) / len(rep):
#                 k += 1
# print(k)



# with open("92.txt") as f:
#     k=0
#     for line in f:
#         a=list(map(int,line.split()))
#         k+=1
#         povt=[]
#         nepovt=[]
#         povt.append(x for x in a if a.count(x)==3)
#         nepovt.append(x for x in a if a.count(x)==1)
#         if len(set(povt))==1 and len(set(nepovt))==4:
#             if sum(nepovt)>sum(povt):
#                 print(k)







