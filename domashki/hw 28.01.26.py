# Создайте декоратор retry(max_retries, delay), который принимает
# два аргумента: максимальное количество попыток и задержку между попытками.
# Декоратор должен принимать от функции возвращаемое значение, и если
# значение False, то запускать функцию снова через количество секунд,
# переданное в параметре delay, пока возвращаемое значение не будет True,
# при этом количество перезапусков не должно превышать значения, переданного
# в параметре max_retries.
# from time import sleep
# from random import choice
# def retry(max_retries, delay):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(max_retries):
#                 if func():
#                     return True
#                 sleep(delay)
#             return False
#         return wrapper
#     return decorator
#
# @retry(max_retries=3, delay=3)
# def check():
#     print("Пробую...")
#     return choice([True, False])
# result = check()
# print("Результат:",result)




