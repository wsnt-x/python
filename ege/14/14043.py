for x in range(1,3000):
    a=9**150+9**30-x
    b = []
    while a:
        b.append(a % 9)
        a //= 9
    if b.count(0) == 122:
        print(x)
        break