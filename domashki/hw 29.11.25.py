# 1.Напишите функцию которая принимает натуральное число а возвращает список его цифр
# def func(a):
#     l=[]
#     for i in a:
#         l.append(i)
#     return l
# print(func(input()))
# 2.Напишите функцию которая принимает текст и именнованные аргументы, и возвращает словарь
# с подсчетом слов с учетом опций, опции задаются через именнованные аргументы
# например, ignore_case = True, придумать 2 опции для посчета слов, опции могут быть не обязательными
def words(text,**options):
    if options.get("ignore_case"):
        text=text.lower()
    text_list:list=text.split()
    text_set=set(text_list)
    dict_new={}
    for text_set_item in text_set:
        dict_new[text_set_item]=text_list.count(text_set_item)
    print(dict_new)
words("Hello World",ignore_case=True)