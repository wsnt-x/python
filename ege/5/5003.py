a = []
for n in range(1, 1000):
    b = f'{n:b}'
    b = b + str(b.count('1') % 2)
    b = b + str(b.count('1') % 2)
    # R = R + str(sum(int(i) for i in R) % 2)
    # R = R + str(sum(map(int, R)) % 2)
    r = int(b, 2)
    if r > 77:
        # a.append(n)
        a+=[n]
print(min(a))