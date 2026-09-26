from itertools import product

with open(r'files/24_8615.txt') as f:
    data = f.readline()

triplets = list(product("ABCDEF", repeat=3))
cnt, ans = 2, 0

for line in zip(data, data[1:], data[2:]):
    if line not in triplets:
        cnt += 1
    else:
        cnt = 2
    ans = max(ans, cnt)

print(ans)
