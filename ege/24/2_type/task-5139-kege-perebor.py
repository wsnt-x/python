with open(r"files/24_5139.txt") as f:
    data = f.readline()

len_data = len(data) - 2
i = ans = cnt = 0

while i < len_data:
    if data[i] in "BCDF" and data[i + 1] in "AEU" and data[i + 2] in "BCDF":
        cnt += 1
        i += 3
    else:
        cnt = 0
        i += 1
    ans = max(ans, cnt)
print(ans)
