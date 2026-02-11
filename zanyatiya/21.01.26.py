# MAP
# map( функция, список(итерируемый объект))
# map это метод который позволяет применить ф-цию
# к каждому элементу последовательности

# def plus5(x):
#     return x + 5
# a=[2,3,4,5]
# # print(list(map(plus5,a)))
# print(list(map(lambda x: [[]]*x, a)))

# user=[{"username":"admin","password":10},
#       {"username":"john","password":15},
#       {"username":"john","password":20}
# ]
# print(list(map(lambda x:x["username"],user)))
# с помощью map получить список username (list[str])

# nums=list(range(0,10))
# enens=list(filter(lambda x:x%2==0,nums))
# print(enens)
# print(nums)
# # filter()


# nums = ['1', '2', '3']
# evens = list(filter(lambda x: int(x) == 0, nums))
# print(nums)
# print(evens)
# def plus():
#     return "+"
# def minus():
#     return "-"
# def nums(fplus, fminus):
#     return fplus(), fminus()
# s={"plus": plus}
# print(nums(plus, minus))
# print(s["plus"]())

# nums=[1,2,3,4,5]
# nums1=list(map(lambda x:x**2,nums))
# print(nums1)

# nums=[1,2,3,4,5,6,7,8,9,10]
# nums1=list(filter(lambda x:x%2!=0,nums))
# print(nums1)

# words=["sdfsd","bsd","csdfsfdsdf","dfsdf"]
# words1=list(map(lambda x: len(x), words))
# print(words1)

# nums=[-5,-2,0,3,7,-1,10]
# a=list(filter(lambda x: x>0 , nums))
# print(a)

# a=[1,1,1,1,1,1,1,1,1]
# b=[2,2,2,2,2,2,2,2,2]
# print(list(map(lambda x,y: x+y,a,b)))

# list1=[1,2,3,4]
# list2=[5,6,7,8]
# print(list(map(lambda x,y: x*y, list1, list2)))

# def is_simple(x):
#     if 0 <= x <= 2:
#         return False
#     for i in range (2, int(x / 2) + 1):
#         if x% i == 0:
#             return True
#     return False
# nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(list(filter(is_simple, nums)))

# def my_map(func, iterable):
#     result = []
#     for item in iterable:
#         result.append(func(item))
#     return result
# nums = ["hello"]
# print(my_map(len, nums))