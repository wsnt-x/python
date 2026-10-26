a = []
for N in range(1, 1000):
    R = f'{N:b}'
    if N % 2 == 0:
        R = '1' + R + '0'
    else:
        R = '11' + R + '11'
    R = int(R, 2)
    if R > 52:
        a.append(R)
print(min(a))