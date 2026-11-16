for x in range(1,2030):
    a=3**100-x
    b=[]
    while a:
        b.append(a%3)
        a//=3
    if b.count(0)==1:
        print(x)