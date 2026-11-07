from math import *
a=10+70
i=ceil(log2(a))
for l in range(1,30):
    idn=ceil(i*l/8)
    if idn*1234567>24*2**20:
        print(l)
        break