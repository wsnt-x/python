# from math import *
# i=ceil(log2(1710))
# idn=ceil(i*252/8)
# a=ceil(4096*idn/1024)
# print(a)

# from math import *
# a=10+999
# i=ceil(log2(a))
# idn = ceil(i * 745 / 8)
# b=312*idn
# perone=(311*1024)/312
# extra=(perone-idn)*312
# print(extra)

# from math import *
# alphabet = 520
# bits = ceil(log2(alphabet))
# id_bytes = ceil(99 * bits / 8)
# total_bytes = 543 * 1024
# users = 4322
# per_user = total_bytes // users +1
# extra_all = (per_user - id_bytes)
# print(extra_all)

from math import *
for i in range(1,1000):
    bit=ceil(log2(i))
    idn=ceil(261*bit/8)
    if 252500 * idn >31*1024*1024:
        print(i)
        break
