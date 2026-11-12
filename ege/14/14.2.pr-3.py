from string import printable
for x in printable[:26]:
    sumi = int(f'27{x}98876',26) + int(f'26{x}51',26) + int(f'15{x}47',26) + int(f'62{x}5',26)
    if sumi%25==0:
        print(sumi//25)
        break