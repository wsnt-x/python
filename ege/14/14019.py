from string import printable
for x in printable[:19]:
    sumi = int(f'98{x}79641',19)+int(f'36{x}14',19) + int(f'73{x}4',19)
    if sumi%18==0:
        print(sumi//18)