#Создайте словарь, где ключами являются числа от 1 до 10, а значениями - их кубы.
# cubes_dict={x:x**3 for x in range(1,11)}
# print(cubes_dict)
#Создайте множество квадратов чисел от 1 до 20.
# a={i**2 for i in range(1,21)}
# print(a)
#Дан список чисел [2, 4, 6, 8, 10]. Проверьте, есть ли в списке хотя бы одно число, которое больше 7 И делится на 3.
# nums=[2,4,6,8,10,12]
# result=any(num>7 and num%3==0 for num in nums)
# print(result)
#Дан пароль password = "MyPass123". Проверьте, что пароль содержит хотя бы
# одну заглавную букву, одну строчную букву и одну цифру.
# password = "MyPass123"
# has_upper=any(char for char in password if char.isupper())
# has_lower=any(char for char in password if char.islower())
# has_digit=any(char for char in password if char.isdigit())
# print(all([has_upper,has_lower,has_digit]))

#3
# with open("901.txt","r") as f:
#     data=[list(map(int, i.split())) for i in f]
# def f1(line):
#     # повторяются 3 раза
#     cnt_3=[i for i in line if line.count(i)==3]
#     # без повторений
#     cnt_1=[i for i in line if line.count(i)==1]
#     return len(cnt_3)==6 and len(cnt_1)==1
# def f2(line):
#     # все повторяющиеся
#     rep=[i for i in line if line.count(i)!=1]
#     # все неповторяющиеся
#     norep=[i for i in line if line.count(i)==1]
#     # среднее арифметическое
#     aver=sum(rep)/len(rep)
#     return aver< norep[0]
# for pos, val in list(enumerate(data,start=1))[::-1]:
#     if f1(val) and f2(val):
#         print(pos)
#         break

#2
# Откройте файл, содержащий в каждой строке
# шесть натуральных чисел.
# Определите наибольший номер строки таблицы,
# для чисел которой выполнены оба условия:
# в строке есть одно число, которое повторяется
# трижды, остальные три числа различны;
# повторяющееся число строки больше, чем среднее
# арифметическое её неповторяющихся чисел.

# with open("911.txt","r") as f:
#     data=[list(map(int,i.split())) for i in f]
# def f1(line):
#     cnt_3=[i for i in line if line.count(i)==3]
#     cnt_1=[i for i in line if line.count(i)==1]
#     return len(cnt_3)==1 and len(cnt_1)==3
# def f2(line):
#     # все повторяющиеся
#     rep=[i for i in line if line.count(i)!=1]
#     # все неповторяющиеся
#     norep=[i for i in line if line.count(i)==1]
#     # среднее арифметическое
#     return rep>(sum(norep)/len(norep))
# for pos, val in list(enumerate(data,start=1))[::-1]:
#     if f1(val) and f2(val):
#         print(pos)
#         break
# from statistics import mean
# with open ('911.txt') as f:
#     data = [list(map(int, i.split())) for i in f]
#
# for pos, val in list(enumerate(data, start=1))[:: -1]:
#     cnt_3 = [i for i in val if val.count (i) == 3]
#     cnt_1 = [i for i in val if val.count (i) == 1]
#     if len(cnt_3) == 3 and len(cnt_1) == 3 and mean(cnt_1) < cnt_3[0]:
#         print (pos)
#         break

# ИЛИ

# stroka = 0
# for line in open("911.txt"):
#     a = list(map(int, line.split()))
#     stroka += 1
#     a1 = [i for i in a if a.count(i) == 3]
#     a3 = [i for i in a if a.count(i) == 1]
#     sr = sum(a3) / len(a3)
#     if len(a1) == 3 and len(a3) == 3:
#         if sr < int(a1[-1]):
#             print(stroka)

#913.txt
# Откройте файл, содержащий в каждой строке пять
# натуральных чисел.
# Определите наибольший номер строки таблицы, для которой
# выполнены оба условия:
# в строке все числа различны;
# удвоенная сумма минимального и максимального
#  чисел строки равна утроенной сумме трёх её оставшихся
#  чисел.
# with open("913.txt") as f:
#     data = [list(map(int, line.split())) for line in f]
# def f1(line):
#     return len(line) == len(set(line))
# def f2(line):
#     line = sorted(line)
#     return (line[0] + line[-1]) * 2 == sum(line[1:-1]) * 3
# max_index = 0
# for i, line in enumerate(data, start=1):
#     if f1(line) and f2(line):
#         max_index = i
# print(max_index)

# открываем файл и считываем данные
with open("название файла") as f:
    data = [list(map(int, i.split())) for i in f]
# Условие 1
def f1(line):
    pass
# Условие 2
def f2(line):
    pass
count = 0
for line in data:
    pass
# если оба условия выполняются
# увеличиваем count на 1
print(count)