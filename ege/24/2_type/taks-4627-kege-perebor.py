with open(r'files/24_4627.txt') as f:
    data = f.readline()

# data = "******NPOPNOPNO"

ans = i = cnt = 0
len_data = len(data)
while i < len_data-1:
    if data[i] + data[i + 1] + data [i + 2] in "PNO NPO":
        cnt += 3
        i += 3
    else:
        cnt =0
        i += 1
    ans = max(ans, cnt)
print(ans//3)
