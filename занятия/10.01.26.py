# b=[]
# for i in range(10):
#     b.append(i)
# print(b)

# or

#[выражение for элемент in последовательность if условие]
# b=[i/10 for i in range(10) if i%2==0]
# print(b)

# nums=[1,2,3,4,5,-4,-5,-1,-2,-3]
# a=[i**2 for i in nums if i>0]
# print(a)

# b=[]
# for i in range(1,4):
#     for j in range(1,4):
#         b.append(i*j)
# print(b)
# matrix=[[i*j for i in range(1,4)] for j in range(1,4)]
# print(matrix)
# flatten_matrix=[item for row in matrix for item in row]

# dict_test={i:i**2 for i in range(1,6)}
# print(dict_test)
# print(dict_test[5])

# set_test={i for i in range(10)}
# print(set_test)

# tuple_test=tuple(i for i in range(1,10))
# print(tuple_test)

# множество пар (x,y) где x и y - числа от 1 до 3, элементы уникальны
# pairs={(x,y) for x in range(1,4) for y in range(1,4)}
# print(pairs)

# a=[i**2 for i in range(1,16)]
# print(a)

# a=["python","java","c++","javascript","go"]
# b=[i.upper() for i in a]
# print(b)

# a=[0,15,25,30,-5,-10]
# b=[i*9/5+32 for i in a if i>0]
# print(b)

# a=[[1,2,3],[4,5,6],[7,8,9]]
# b=[j for i in a for j in i if j%2==0]
# print(b)

# Дан список слов ['apple', 'banana', 'cherry', 'date', 'elderberry'].
# Создайте словарь, где ключ - слово, значение - его длина,
# но только для слов длиной больше 5 символов.
# a=['apple', 'banana', 'cherry', 'date', 'elderberry']
# b={i:len(i) for i in a if len(i)>5}
# print(b)

# Дан список строк ['Привет мир!',
# 'Программирование', 'Списочные включения'].
# Создайте словарь, где ключ - строка, значение -
# список длин каждого слова в этой строке.
# a = ['Привет мир!', 'Программирование', 'Списочные включения']
# b = {i: [len(word) for word in i.split()] for i in a}
# print(b)

# Создайте словарь, где ключи - числа
# от 1 до 5, а значения - списки делителей
# этого числа (включая 1 и само число).

# a={i:[j for j in range(1,i+1) if i%j==0] for i in range(1,6)}
# print(a)

# Дан список списков [[2, 4, 6], [8, 10, 12], [14, 16, 18]].
# Проверьте, все ли подсписки содержат только четные числа.
# a=[[2, 4, 6], [8, 10, 12], [14, 16, 18]]
# print(all(j%2==0 for i in a for j in i ))
