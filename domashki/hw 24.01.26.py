# 1. Создайте функцию с замыканием make_stats_tracker(),
# которая возвращает четыре функции: для добавления числа,
# получения среднего значения, получения минимума и максимума.
# Функция должна эффективно отслеживать все необходимые статистики.
# def make_stats_tracker():
#     count=0
#     total=0
#     mx=None
#     mn=None
#     def f1(x):
#         nonlocal count,total,mx,mn
#         count+=1
#         total+=x
#         if mn is None or x<mn:
#             mn=x
#         if mx is None or x>mx:
#             mx=x
#         return total
#     def f2():
#         return total/count #if count!=0 else 0
#     def f3():
#         return mn
#     def f4():
#         return mx
#     return f1,f2,f3,f4
# f1,f2,f3,f4=make_stats_tracker()
# f1(3)
# print(f1(4))
# print(f2())
# print(f3())
# print(f4())
# 2. Создайте функцию с замыканием make_task_manager(), которая
# возвращает набор функций для управления задачами: добавление задачи,
# пометка задачи как выполненной по ID, получение списка всех задач,
# получение списка невыполненных задач и получение статистики. Каждая
# задача должна иметь уникальный ID, название и статус выполнения.
# def make_task_manager():
#     tasks = []
#     next_id=1
#     def add_task(title):
#         nonlocal next_id,tasks
#         task={"id":next_id,"title":title,"finished":False}
#         tasks.append(task)
#         next_id+=1
#     def complete_task(task_id):
#         nonlocal tasks
#         for task in tasks:
#             if task["id"] == task_id:
#                 task["finished"] = True
#                 return task
#         return None
#     def get_all_tasks():
#         nonlocal tasks
#         return tasks
#     def unfinished_tasks():
#         return [task for task in tasks if not task["finished"]]
#     def get_stats():
#         total=len(tasks)
#         done=sum(1 for task in tasks if task["finished"])
#         q=total-done
#         return {"total":total,"done":done,"left":q}
#     return add_task,complete_task,get_all_tasks,unfinished_tasks,get_stats
# add_task, complete_task, get_all_tasks, unfinished_tasks, get_stats = make_task_manager()
# add_task("сделать домашку по программированию")
# complete_task(1)
# print(get_all_tasks())
# add_task("сделать уроки")
# print(unfinished_tasks())
# print(get_stats())
# 3. Напишите функцию apply_to_each(numbers, operation), которая
# принимает список чисел и функцию-колбэк, применяет эту функцию
# к каждому элементу списка и возвращает новый список с результатами.
# Протестируйте её с функциями возведения в квадрат и удвоения числа.
# def apply_to_each(numbers, operation):
#     result=[]
#     for n in numbers:
#         processed=operation(n)
#         result.append(processed)
#     return result
#     pass
# def square(number):
#     return number ** 2
# numbers=[1,2,3]
# square_result=apply_to_each(numbers, square)
# print(square_result)