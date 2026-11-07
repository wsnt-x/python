from math import *

a=10+52+458
i=ceil(log2(a))
for l in range(1,1000):
    idn=ceil(i*l/8)
    if idn*862<=276*2**10:
        print(l)