#29
# from random import *
# a=[]
# for i in range(5):
#     a.append(randint(0,9))
# print(a)
# a[0],a[-1]=a[-1],a[0]
# print(a)
#25
# nums=[1,2,3,4,5,6]
# a=int(sum(nums)/len(nums))
# for i in nums:
#     if i==a:
#         nums.remove(i)
# print(nums)
#23
# a=[1,1,2,5,4,6,7,8]
# for i in range(1,len(a)-1):
#     if a[i]>a[i+1] and a[i]>a[i-1]:
#         k=[a[i],i]
#         break
# print(k[0], k[1], a.index(k[0]))
#21
# a=input().split(' ')
# h=[]
# for i in a:
#     if i not in and a.count[i]<2:
#         h.append(i)
# print(h)
#31
a=[2,4,2,9,8,3,4,1,9,3,2,8,5,9]
maxim=0
cash=[]
for i in range(len(a)):
    seen=[]
    for j in range(i,len(a)):
        if a[j] in seen:
            break
        seen.append(a[j])
if len(seen)>maxim:
    maxim=len(seen)
    cash=seen
print(maxim, sum(cash), cash)