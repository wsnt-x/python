from math import *

a=10+52+963
i=ceil(log2(a))
for l in range(1,1000):
    idn=ceil(i*l/8)
    if 2000*idn<=693*2**10:
        print(l)