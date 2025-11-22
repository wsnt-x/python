#85
# a=set(input().split())
# b=set(input().split())
# da=dict.fromkeys(a,0)
# db=dict.fromkeys(b,0)
# for i in a:
#     da[i]+=1
# for i in b:
#     db[i]+=1
# for key,value in da.items():
#     if key not in db:
#         db[key]=value
#     else:
#         db[key]+=value
# print(da)
# print(db)

#86
# a=sorted(input().split())
# dict_a=dict.fromkeys(a,0)
# dict_b={}
# for i in dict_a:
#     dict_a[i]=a.count(i)
#     if dict_a[i]>1:
#         dict_b.update({i:dict_a[i]})
# print(dict_a)
# print(dict_b)

#88
# students = [
#
#     {'name': 'Alice', 'group': 'A', 'score': 85},
#
#     {'name': 'Bob', 'group': 'B', 'score': 92},
#
#     {'name': 'Charlie', 'group': 'A', 'score': 78},
#
#     {'name': 'David', 'group': 'C', 'score': 88},
#
#     {'name': 'Eve', 'group': 'B', 'score': 95}
#     ]
# s={}
# for student in students:
#     if student['group'] in s:
#         s[student['group']].append(student['name'])
#     else:
#         s[student['group']] = [student['name']]
# print(s)

#87
a=input().replace(" ","")
b={}
for i in a:
    b[i]=a.count(i)
s=[["",0]*3]
for i in b:
    for j in range(len(s)):
        if s[j][1]<b[i]:
            s[j][0]=i
            s[j][1]=b[i]
            break
print(b)
print(s)
#доделать