# def a(text):
#     def b(t):
#         print(t+text)
#     return b("Hello")
# # b("Hello") нельзя
# a("world")

# def a(name,func):
#     print(name)
# a("борис", lambda x:x*2)

# def create_discount(category):
#     def bronze(price):
#         return price * 2
#     def silver(price):
#         return price * 0,5
#     def gold(price):
#         return price * 0,1
#     if category == 'bronze':
#         return bronze
#     elif category == 'silver':
#         return silver
#     elif category == 'gold':
#         return gold
# bronze_discount = create_discount('bronze')
# product_price=1000
# print(f'{bronze_discount(product_price)}')

# def count_10_times(nums):
#     if nums>=10
#         return nums
#     return count_10_times(nums+1)
# print(count_10_times(1))

# name="Hello"
# def a():
#     # global name
#     name2="world"
#     def next():
#         # nonlocal name
#         name2="123"
#     next()
#     print(name2)
# a()

# def create_adder(number):
#     def add_to(x):
#         return x+number
#     return add_to
#
# add_five=create_adder(5)
# add_ten=create_adder(10)
# print(add_five(10))
# print(add_five(7))
# print(add_five(7))
# print(add_ten(10))
# print(add_ten(10))
# print(add_ten(10))

# def create_adder (number):
#     count = 0
#     def add_to():
#         nonlocal count
#         count += 1
#         return count
#     return add_to
# add_one = create_adder (5) #замыкания
# print(add_one())
# print(add_one))
# print(add_one))
# print(add_one())
# print(add_one())

# def make_even_generator(start):
#     # current=start if start%2==0 else start+1
#     def next_even():
#         nonlocal start
#         result = start
#         start += 2
#         return result
#     return next_even
# even_gen=make_even_generator(6)
# print(even_gen())
# print(even_gen())
# print(even_gen())


# def make_string_builder(z):
#     def f(s):
#         nonlocal z
#         z = z + " " + s
#         return z
#     return f
#
# q = make_string_builder("")
# print(q("one"))
# print(q("two"))

# def make_product_accumulator():
#     p = 1
#     def f(x):
#         nonlocal p
#         p *= x
#         return p
#     return f
# a = make_product_accumulator()
# print(a(2))
# print(a(3))
# print(a(4))

# def make_counter(start,step):
#     def increment():
#         nonlocal start
#         start += step
#         return start
#     return increment
# q=make_counter(0,1)
# print(q())
# print(q())


# def create_lenght_filter(min_lenght):
#     def f(x):
#         nonlocal min_lenght
#         return len(x) >= len(min_lenght)
#     return f
# a=create_lenght_filter("qwer")
# print(a("qwerty"))


# def create_formatter(prefix, suffix):
#     def f(x:str):
#         nonlocal prefix, suffix
#         return f'{prefix}{x}{suffix}'
#     return f
# a=create_formatter(prefix='p', suffix='n')
# print(a("ytho"))


# Создайте функцию с замыканием make_stats_tracker(),
# которая возвращает четыре функции: для добавления числа,
# получения среднего значения, получения минимума и максимума.
# Функция должна эффективно отслеживать все необходимые статистики.
# from statistics import *
# def make_stats_tracker():
#     c=0
#     def f1(x):
#         nonlocal c
#         c+=x
#         return c
#     return f1
#     def f2(x):
#         nonlocal c
#         return mean(x)
#     return f2
#
# a=make_stats_tracker()
# print(a(5))
# print(a(5))