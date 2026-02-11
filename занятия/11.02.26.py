# 1
# data = """2024-01-10, Аренда, 8000.00
# 2024-01-12, Продукты, 4500.50
# 2024-01-14, Транспорт, -2000.00
# 2024-01-16, Продукты, 5000.30
# 2024-01-18, Налог, -350.50
# 2024-01-20, Доставка, -650.00
# 2024-01-22, Аренда, 8000.00
# 2024-01-24, Продукты, 3600.52
# 2024-01-26, Транспорт, -2500.00
# 2024-01-28, Зарплата, 5000.00
# 2024-01-30, Налог, -120.50"""
# print("╔══════════════════════════════════════════════════════════╗")
# print("║                     ФИНАНСОВЫЙ ОТЧЕТ                     ║")
# print("╠══════════════════════════════════════════════════════════╣")
# total = 0
# for line in data.split("\n"):
#     a, b, c = line.split(", ")
#     c = float(c)
#     total += c
#     print(f"║ {a.ljust(10)} │ {b.center(12)} │ {str(c).rjust(10)} ₽                 ║")
# print("╠══════════════════════════════════════════════════════════╣")
# print(f"║ {'ИТОГО:'.ljust(24)} {str(total).rjust(10)} ₽                    ║")
# print("╚══════════════════════════════════════════════════════════╝")

# 2
# with open("access.txt") as f:
#     lines = f.readlines()
#     print(lines)
# a200 = [line.split()[0] for line in lines if "200" in line]
# b401 = [line.split()[0] for line in lines if "401" in line]
# c403 = [line.split()[0] for line in lines if "403" in line]
# d404 = [line.split()[0] for line in lines if "404" in line]
# e500 = [line.split()[0] for line in lines if "500" in line]
# print(a200)
# print(b401)
# print(c403)
# print(d404)
# print(e500)

#3
# k=0
# with open("triples.txt") as f:
#     s=f.readlines()
#     for line in range(len(s)-2):
#         a,b,c=int(s[line]),int(s[line+1]),int(s[line+2])
#         triple=[a,b,c]
#         if any(x%5==(min(triple)) for x in triple):
#             k+=1
# print(k)

# 4
# ...

# 5
# def log_action(func):
#     def wrapper(*args, **kwargs):
#         print(f"Выполняется {func.__name__}...")
#         result = func(*args, **kwargs)
#         print(f"Функция {func.__name__} завершена.\n")
#         return result
#     return wrapper
# @log_action
# def read_file():
#     with open("transactions.txt") as f:
#         return [line.strip().split(",") for line in f if line.strip()]
# @log_action
# def get_total_by_category(sales, category):
#     return sum(float(amount.strip()) for _, cat, amount in sales if cat.strip() == category)
# @log_action
# def get_average(sales):
#     return sum(float(amount.strip()) for _, _, amount in sales) / len(sales)
# sales = read_file()
# total = get_total_by_category(sales, "Продукты")
# print(f"Общая сумма по категории 'Продукты': {total} ₽\n")
# average = get_average(sales)
# print(f"Средняя сумма по всем данным: {average} ₽")

