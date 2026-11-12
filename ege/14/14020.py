from string import printable

for x in printable[:22]:
    sumi = int(f'18{x}89957',22) + int(f'80{x}33',22) + int(f'521{x}6',22)
    if sumi%21==0:
        print(sumi//21)
        break