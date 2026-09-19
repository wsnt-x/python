data = '**ABACACAB********************ABACAB***AB***ABABABABABAB'

ans = cnt = i = 0
len_data = len(data)

while i < len_data-1:
    if data[i] + data[i + 1] in 'AB AC':
        cnt += 1
        i += 2
    else:
        cnt = 0
        i += 1
    ans = max(cnt, ans)
print(ans)
