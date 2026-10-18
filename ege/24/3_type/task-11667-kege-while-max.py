with open(r"files/24_11667.txt") as f:
    data = f.readline()

l = r = cnt = ans = 0
len_data = len(data)

while r < len_data:
    if cnt <= 1:
        if data[r : r + 8] == "INFINITY":
            cnt += 1
        r += 1
    else:
        if data[l : l + 8] == "INFINITY":
            cnt -= 1
        l += 1
    print(l, r, r - l, data[l : r + 1])
    ans = ans(max(ans, r - l + (6 if r != len_data else 0)))

print(ans)
