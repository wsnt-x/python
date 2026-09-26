with open(r"files/24_1273.txt") as f:
    data = f.readline()

ans, cnt = 0, 2
len_data = len(data)

for i in range(len_data - 2):
    if data[i : i + 3] != "XYZ":
        cnt += 1
    else:
        cnt = 2
    ans = max(ans, cnt)

print(ans)
