# lambda аргументы: тело функции (выражение)
# square= lambda x: x** 2
# print(square(5))

# numbers= [-1,2,-3,4,5]
# def double_pos(num):
#     if num >0:
#         return num*2
#     return num
# double_pos= lambda num: num*2 if num>0 else num
# pos_doubled= [double_pos(i) for i in numbers]
# print(pos_doubled)

# pos_doubled=list((lambda num: num*2 if num>0 else num)(number) for number in numbers)
# print(pos_doubled)

# dict_students=[
#     {"name":"John","age":25,"grade":"10"},
#     {"name":"Борис","age":10,"grade":"1"},
#     {"name":"Аркадий","age":30,"grade":"4"}
# ]
# get_name=lambda student: student.get("name")
# get_age=lambda student: student.get("age")
# get_student=lambda student: student.get("grade") if student.get("grade") > 3 else None
# names=[get_name(student) for student in dict_students]
# ages=[get_age(student) for student in dict_students]
# grades=[get_student(student) for student in dict_students if get_student(student)]
# print(names)
# print(ages)
# print(grades)
#
# unsorted_list=[4,3,2,5,1]
# print(sorted(unsorted_list))
#
# unsorted_str="ZV-bc-aA"
# print(sorted(unsorted_str))
#
# unsorted_dict={4:"qwe",5:"asd",3:"SD"}
# print(sorted(unsorted_dict))

# words=['maksim','my','name']
# sorted_list=sorted(words,key=len)
# print(sorted_list)

# nums=[14,5,23,41,2]
# sorted_nums=sorted(nums,key=lambda x: x%10)
# print(sorted_nums)

# students=[("John",98),("Michael",77),("Bob",92.txt),("Robert",84),("Kevin",85)]
# print(sorted(students, key= lambda x: x[1]))

# dict_students = [
# {"name": "John", "age": 25, "score": 98},
# {"name": "Борис", "age": 10, "score": 77},
# {"name": "Аркадий", "age": 30, "score": 92.txt},
# {"name": "hellokitty", "age": 30, "score": 84},
# {"name": "АркадийПаровозов", "age": 30, "score": 85}
# ]

#[::-1] / reverse=True
#
# a=sorted(dict_students, key=lambda student: -student["score"], reverse=True)
# print(a[::-1])

# students={
#     ("alice",4),
#     ("boris",5),
#     ("victor",4),
#     ("galina",3),
#     ("dima",5),
#     ("elena",3),
# }
# students_sorted=sorted(students,key=lambda student: student[1],reverse=True)
# for name,grade in students_sorted:
#     print(f"{name}: оценка {grade}")

# a="JavaScript_govno"
# b=lambda x: len(x)*8
# print(b(a))

# is_even=lambda x : x%2==0
# print(is_even(4))
# print(is_even(7))

# Создайте обычную функцию my_logger(), которая принимает лямбда-функцию и целое число.
# Эта функция должны выводить следующее сообщение:
# undefined
# Пользователь применяет свою функцию.
# Передано число: {num}.
# Результат: {result}
# Создайте лямбда-функцию для возведения числа в третью степень и
# передайте ее в функцию my_logger() вместе с числом 5.
# def my_logger(func,num):
#     print(f"передано число: {num}.\n"
#           f"результат: {func(num)}"
#           )
# my_logger(lambda x: x**3, 5)

# data=[(1,"b"),(3,"a"),(2,"c")]
# print(sorted(data,key=lambda x:x[1]))

