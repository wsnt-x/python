c=[]
for x in range(1,3001):
    a=4**210+4**110-x
    b=[]
    while a:
        b.append(a%4)
        a//=4
    c.append([b.count(0),x])
print(max(c,key=lambda x: [x[0],-x[1]]))