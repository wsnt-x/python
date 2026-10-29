for n in range(1,1000):
    b=f'{n:o}'
    if sum(b.count(i) for i in '0246')%2!=0:
        b=b[-3:]+'46'
    else:
        b=str(f'{n%8*5}')+b
    r=int(b,8)
    if r==n:
        print(n)
        break