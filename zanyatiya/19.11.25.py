# sets={"key":"value","key1":[1,2,3,4]} #словарь с элементом {ключ:значение}
# print(sets["key"])
# print(sets["key1"][2])
# my_dict=[("ключ1","значение1"),("ключ2","значение2"),("ключ1","значение1")]
# print(my_dict,dict(my_dict))
# d={}#dict
# d={1,2}#set
# b={str([1,2,3]):3,3:5}
# print(b[3])
# d={"key1":"value1"}
# # print("key1" in d )#если ли в словаре d?
# b=[1,2,3]
# d["key1"]=100
# d["key2"]=1000
# print(d)
# del d["key1"]
# print(d)
# d={"key1":"value1","key2":"value2"}
# for i in d:
#     print(d[i])

# print(list(d.items()))#получаем все эл-ты словаря как список кортежей
# for i,j in d.items():
#     print(i,j)
# print(list(d.values())) #возвращает список значений
# print(list(d.keys())) #возвращает список ключей

# print(d.get("key3",10)) #get(key, value if doesnt exist)
# print(d.pop("key3",10),d)#удаляет эл-т и возвращает значение
# print(d.popitem())#удаляет и возвращает последний элемент

# d.update({"key3":"value3"})
# print(d)

# d.clear()

# d={"key1":"value1","key2":"value2"}
# # a=d
# a=d.copy()#создает копию эл-та в памяти
# a["key3"]="value100"
# print(d,a)

# keys=["key1","key2","key3","key4"]
# new_dict=dict.fromkeys(keys,10)
# print(new_dict)

#69
# a={}
# a.update({"name":"alice"})
# a["name"]="alice"
# print(a)

#71
# points={"x":10}
# print(points.get("y",0))

#72
# books={"романы":10,"детективы":5}
# # books.update({"фантастика":8})
# books["фантастика"]=8
# print(books)

#79
# marks = {"Информатика":5,
#
#          "Математика":5,
#
#          "Русский":3,
#
#          "История":4,
#
#          "Физика":4}
# print(sum(marks.values())/len(marks))

#80
#a:100 b:200 c:10
# s={}
# k=[]
# a=input().split()
# for i in a:
#     key,value=i.split(":")
#     k.append((key,int(value)))
#     s[key]=int(value)
# print(s,"\n",dict(k))

#81
students=["anna",5,"boris",4,"vera",5]
s={}
for i in range(0, len(students),2):
    s[students[i]]=students[i+1]
print(s)