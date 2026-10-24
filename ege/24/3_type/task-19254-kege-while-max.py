with open(r"files/24_19254.txt") as f:
    data = f.readline()

# data = "**FSRQ****FSRQ***FSRQ*FSRQ***"

l = r = cnt = ans = 0
len_data = len(data)

while r < len_data:
    if cnt <= 80:
        if data[r : r + 4] == "FSRQ":
            cnt += 1
        r += 1
    else:
        if data[l : l + 4] == "FSRQ":
            cnt -= 1
        l += 1
    ans = max(ans, r - l + (2 if r != len(data) else 0))

print(ans)
