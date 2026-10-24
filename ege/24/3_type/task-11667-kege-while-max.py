with open(r"files/24_11667.txt") as f:
    data = f.readline()

l = r = cnt = ans = 0
len_data = len(data)

while r < len_data - 8:
    if cnt <= 1000:
        if data[r : r + 8] == "INFINITY":
            cnt += 1
        r += 1
    else:
        if data[l : l + 8] == "INFINITY":
            cnt -= 1
        l += 1
    if cnt == 1000:
        ans = max(ans, r - l + 7)
print(ans)
