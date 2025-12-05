# 1.Создайте файл в режиме 'w' с текстом "Привет\nКак дела\n".
# Затем в режиме 'a' добавьте строку "Как погода\n" с помощью write().
# Прочитайте весь файл в режиме 'r' с помощью readlines() и выведите список строк.

# with open("hw.txt","w") as f:
#     f.write("Привет\nКак дела\n")
# with open("hw.txt","a") as f:
#     f.write("Как погода\n")
# with open("hw.txt","r") as f:
#     print(f.readlines())

# 2. Дан словарь:
# python
# {"A": 10, "B": 20, "C": 30}
# Замените ключи на случайные трехзначные числа.
# Запишите полученный словарь в файл в режиме 'w', каждую
# пару ключ-значение на новой строке в формате "ключ:значение\n". Затем
# прочитайте файл в режиме 'r' с помощью readlines() и выведите пары.
# from random import randint
# d = {"A": 10, "B": 20, "C": 30}
# for key in d:
#     d[key] = randint(100, 999)
# with open("hw2.txt", "w") as f:
#     for item in d:
#         f.write(f"{item} : {d[key]}\n")
# with open("hw2.txt", "r") as f:
#     print(f.readlines())
# 3. Создайте файл в режиме 'w' с 50 строками случайных
# чисел от 1 до 100. В режиме 'a' добавьте 20 строк. Прочитайте
# все в режиме 'r' с readlines() и выведите сумму всех чисел.
from random import randint
with open("hw3.txt","w") as f:
    for i in range(50):
        f.write(str(randint(0,100)))
with open("hw3.txt","a") as f:
    for i in range(20):
        f.write(str(randint(0,100)))
with open("hw3.txt","r") as f:
    a=f.readlines()
    s=0
    for i in a[0]:
        s=s+int(i)
    print(s)

