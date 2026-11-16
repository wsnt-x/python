c=[]
for x in range(1,2030):
    a=5**150+5**100-x
    b = []
    while a:
        b.append(a % 5)
        a //= 5
    c.append([b.count(0),x])
print(max(c,key=lambda q:(q[0],q[1])))