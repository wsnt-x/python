# def per3(num,sys):
#     res=''
#     while num:
#         res=str(num%sys)+res
#         num//=sys
#     return res if res else '0'

from string import printable
def convert(num,sys):
    res=''
    while num:
        res=printable[num%sys]+res
        num//=sys
    return res if res else '0'

for n in range(1,1000):
    b=convert(n,3)
    if n%3==0:
        b='1'+b+'02'
    else:
        b=b+str(convert(n%3*4,3))
    r=int(b,3)
    if r<199:
        print(n)

