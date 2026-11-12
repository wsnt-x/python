from string import printable

for x in printable[:20]:
    sumi = int(f'627{x}j8',20) + int(f'h45i{x}5hij',20) + int(f'4idb49j{x}7',20)
    if sumi%19==0:
        print(sumi//19)

