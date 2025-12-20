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













