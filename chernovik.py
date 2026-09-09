from math import *

l = 303
a = 8190+10
i=ceil(log2(a))
for x in range(10000):
    idn=ceil(i*l/8)+x
    if 101*idn<=101*2**10:
        print(x)
