from string import printable
ans=[]
for x in range(10,14):
    for y in range(9,x):
        sumi = int(f'7{printable[x]}37{printable[y]}',14) + int(f'9{printable[y]}63',x) - int(f'15148',y)
        ans.append(sumi)
        if sumi==316323:
            print(sumi//(x+y))

