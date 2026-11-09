k=0
for a in range(1,1000):
    a5=[]
    b=c=a
    while a:
        a5.append(a%5)
        a//=5
    a3=[]
    while b:
        a3.append(b%3)
        b//=3
    a16=[]
    while c:
        a16.append(c%16)
        c//=16
    if a16[0]==13 and len(a5)==4 and len(a3)==5:
        k+=1
print(k)