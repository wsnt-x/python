a = []
for n in range(1, 1000):
    b = f'{n:b}'
    if n % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    r = int(b, 2)
    if r > 441:
        # a.append(n)
        a += [n]
print(min(a))
