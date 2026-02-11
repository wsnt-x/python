#открытие файла (маршрут) / тип открытия / кодировка при чтении / записи
# file=open("test.txt","r",encoding="utf-8")
# print(file)
# print(file.read()) #считывает все строки текстового файла

# r - чтение
# w - запись
# a - добавлять в конец файла
# x - открывает файл для записи только если он не существует
# rb, wb, ab, xb - бинарные действия
# r+/x+ - открывает файл для чтения и записи (файл должен существовать)
# w+/a+ - открывает файл для записи если файла нет он его создаст

# print(file.readline()) #считывает 1 строку из файла
# print(file.readlines()) #считывает файл как список строк

# print(file.readline()) #курсор в начале первой строки
# print(file.readline()) #курсор в начале второй строки
# print(file.readline()) #курсор в начале третьей строки
# print(file.readline()) #курсор в начале четвертой строки

# print(file.read(10))
# print(file.tell()) #позиция указателя (число)
# file.seek(0) #сдвиг "курсора"
# print(file.read(10))
#
# file.close() #каждый раз при открытии мы обязаны закрыть файл

# контекстный менеджер
# with open("test.txt","r",encoding="utf-8") as file:
#     # file_item=file.readline()
#     # while file_item:
#     #     print(len(file_item)-1)
#     #     file_item=file.readline()
#     for file_item in file:
#         print(len(file_item)-1)

# with open("words.txt","w+",encoding="utf-8") as file:
#     file.write("\nhello world")
#
# with open("words.txt","r+",encoding="utf-8") as file:
#     file.write("\nhello world")

# s=["hello\n", "world"]
# with open("test2.txt","w+",encoding="utf-8") as file:
#     file.writelines(s)

#1

# li=["sdfsdf\n","sdfsdf\n","dsfsdf\n"]
# with open("qweqwe.txt","w+",encoding="utf-8") as file:
#     file.writelines(li)
# with open("qweqwe.txt","r",encoding="utf-8") as file:
#     print(file.read())

#2
# a='Привет\nКак дела\n'
# with open("задание2.txt","w+",encoding="utf-8") as file:
#     file.write(a)
# b="Как погода\n"
# with open("задание2.txt","a",encoding="utf-8") as file:
#     file.write(b)
# with open("задание2.txt","r",encoding="utf-8") as file:
#     print(file.readlines())