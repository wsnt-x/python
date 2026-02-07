# def a():
#     print("Hello")
# a()
# print("World")
# процессы (ресурсы/память/файлы/соединения) -> queue []
# потоки -> (ресурсы от процесса/ быстрее создаются и переключаются/ могут обмениваться данными)
# важность процессов ->
# макароны и пожарить мясо
# сначала варим макароны 4 минуты
# потом пожарить мясо 4 минуты
# итого 8 минут

# варить макароны - 2 мин
# пожарить мясо в течение макарон -> (3 мин)

# параллелизм
# 2 мин -> ядра процессора

# import asyncio
# async with async for
#
# async def f():
#     print("Привет")
#     await asyncio.sleep(1)
#     print("Мир")
#
# asyncio.run(f())

# def sync_f():
#     return "result"
# async def async_f():
#     return "result"
# # print(sync_f())
# # print(async_f())
# asyncio.run(async_f())

# async def one(num):
#     print("f_1 start")
#     await asyncio.sleep(num)
#     print("f_1 end ")
#
# async def two(num):
#     print("f_2 start")
#     await asyncio.sleep(num)
#     print("f_2 end ")
#
# async def main():
#     results=await asyncio.gather(one(10), two(1))
#     print(results)
#     # task1=asyncio.create_task(one())
#     # task2 = asyncio.create_task(two())
#     # while True:
#     #     await asyncio.sleep(1)
#     #     task1.cancel()
#     #     if task2.done():
#     #         print("HELLO")
# asyncio.run(main())


# async def download_page(url):
#     print(f"Загружаю {url}")
#     await asyncio.sleep(1)
#     return f"содержимое url: {url}"
# async def main():
#     urls=["https://www.python.org/",
#           "http://www.python.org/about",
#           "http://www.python.org/about3"
#           ]
#     task=asyncio.create_task(download_page(urls[0]))
#     pages= await asyncio.gather(*[download_page(url) for url in urls])
#     print(f"Загружено {len(pages)} страниц")
#     for content in pages:
#         print(content)
# asyncio.run(main())

# 1
# import asyncio
# async def make_coffee():
#     print("начало готовки")
#     await asyncio.sleep(2)
#     print("кофе сделано")
# async def make_toaster():
#     print("начало готовки")
#     await asyncio.sleep(2)
#     print("тост сделан")
# async def main():
#     result = await asyncio.gather(make_coffee(), make_toaster())
#     print(result)
# asyncio.run(main())