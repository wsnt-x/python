# 1.Даны списки
# keys = ['name', 'age', 'city', 'profession']
# values = ['Иван', 28, 'Москва', 'Программист']
# Создайте словарь из этих списков и выведите его
# элементы с номерами строк. Используйте zip и enumerate
# keys = ['name', 'age', 'city', 'profession']
# values = ['Иван', 28, 'Москва', 'Программист']
# my_dict = {}
# for i,j in zip(keys, values):
#     my_dict[i] = j
# print(my_dict)
# for i,(key,value) in enumerate(my_dict.items(),start=1):
#     print(f"{i} {key}:{value}")
# 2.
# Даны два списка ответов: correct_answers = ['A', 'B', 'C', 'D', 'A']
# (верные) и student_answers = ['A', 'B', 'D', 'D', 'A'] (ответы ученика).
# Подсчитайте количество правильных ответов среди ответов ученика и выведите детальную информацию.
# correct_answers = ['A', 'B', 'C', 'D', 'A']
# student_answers = ['A', 'B', 'D', 'D', 'A']
# k = 0
# for i, (correct, student) in enumerate(zip(correct_answers, student_answers), start=1):
#     if correct == student:
#         k += 1
#         result = "верно"
#     else:
#         result = "неверно"
#     print(f"{i}. правильный: {correct}, ответ ученика: {student} => {result}")
# print("Количество правильных ответов:", k)
# 3.Дан список списков [[2, 4, 6], [8, 10, 12], [14, 16, 18]]. Проверьте,
# все ли подсписки содержат только четные числа.
# a = [[2, 4, 6], [8, 9, 12], [14, 16, 18]]
# result = all(num % 2 == 0 for sublist in a for num in sublist)
# print(result)
# 4.
# # Дан список температур [20, 22, 18, 25, 19, 21]. Увеличьте каждую температуру
# # на значение, равное её индексу, и выведите результат.
# a=[20, 22, 18, 25, 19, 21]
# b=[]
# for i,item in enumerate(a):
#     b.append(item+i)
# print(b)
# 5.
# Дана матрица matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]. Проверьте,
# содержит ли каждая строка хотя бы один ноль и есть ли ноль хотя бы в
# одной строке. Если есть, выведите индексы строк с нулями.
# matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
# b=[]
# for i,values in enumerate(matrix):
#     z=i if 0 not in values else ""
#     if 0 in values:
#         print(i)
#         b.append(True)
#     else:
#         b.append(False)
# print(all(b))
