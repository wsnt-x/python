a=[]
for n in range(1,1000):
    b=f'{n:b}'
    if b.count('1')%2==0:
        b='1'+b[2:]+'0'
    else:
        b='11'+b[2:]+'1'
    r=int(b,2)
    if r>25:
        a+=[[r,n]]
print(min(a))