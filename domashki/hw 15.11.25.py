# 1.
# Список заполняется 20 псевдослучайными
# целыми числами в диапазоне от 1 до 7.
# На экран выводится множество уникальных
# элементов.
# Выводится количество повторяющихся
# элементов (разность между длиной исходного
# списка и множества).
from random import *
a=[]
for i in range(7):
    a.append(randint(1,7))
print(a)
print(set(a))
print(len(a)-len(set(a)))
# 2. Создайте программу для работы с множеством:
# Начните с пустого множества my_set.
# В цикле 5 раз запрашивайте у пользователя число.
# Добавляйте каждое число в множество с
# помощью add().
# После окончания ввода выведите итоговое
# множество и количество его элементов.
# Найдите минимальное и максимальное значения в
# множестве.
my_set=set()
for i in range(5):
    x=int(input())
    my_set.add(x)
print(my_set)
print(len(my_set))
my_set=list(my_set)
print("max:",max(my_set))
print("min:",min(my_set))
# 3.
# У вас есть множество numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9,
# 10}. Напишите программу, которая:
# Удаляет все четные числа из множества,
# используя метод discard() в цикле.
# Добавляет квадраты всех оставшихся чисел.
# Выводит итоговое множество
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9,10}
for i in range(len(numbers)):
    if i%2==0:
        numbers.discard(i)
for i in range(len(numbers)):
    if i%2==0:
        for i in range(len(numbers)):
            if i % 2 == 0:
                numbers.add(i**2)
print(numbers)
# 4.
# У вас есть три множества участников книжного клуба, читающих
# разные жанры книг:
# fantasy_ readers = {"Игорь", "Катя", "Лев", "Марина"}
# detective_ readers = {"Катя", "Лев", "Никита", "Ольга"}
# sci _fi _ readers = {"Лев", "Марина", "Никита", "Павел"}
# Найдите:
# Участников, которые читают книги всех трёх жанров.
# Участников, которые читают только фантастику.
# Участников, которые читают ровно два жанра
#
# Сделать любые 3, если будет желание все 4
fantasy_readers = {"Игорь", "Катя", "Лев", "Марина"}
detective_readers = {"Катя", "Лев", "Никита", "Ольга"}
sci_fi_readers = {"Лев", "Марина", "Никита", "Павел"}
print(fantasy_readers&detective_readers&sci_fi_readers)
print(fantasy_readers - detective_readers - sci_fi_readers)
print(((fantasy_readers & detective_readers)-sci_fi_readers ) |
    ((fantasy_readers & sci_fi_readers)-detective_readers) |
    ((detective_readers & sci_fi_readers)-fantasy_readers))


