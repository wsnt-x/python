with open(r'files/24_4602.txt') as f:
    data = f.readline()

# data = "******BOBOBOBO*****"

ans = i = cnt = 0
len_data = len(data)
while i < len_data-1:
    if data[i] + data[i + 1] in "BA BO CA CO DA DO":
        cnt += 2
        i += 2
    else:
        cnt =0
        i += 1
    ans = max(ans, cnt)
print(ans//2)
