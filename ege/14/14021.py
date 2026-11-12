from string import printable

for x in printable[:23]:
    sumi = int(f'7{x}38596',23) + int(f'14{x}36',23) + int(f'61{x}7',23)
    if sumi%22==0:
        print(sumi//22)
        break
