with open("files/24_21717.txt") as f:
    data = f.readline()

data = data.split("RSQ")

ans = 10**10
for i in range(1, len(data) - 129):
    line = "RSQ" + "RSQ".join(data[i : i + 129]) + "RSQ"
    next_line = data[i + 129]
    # for j in range(len(next_line)):
    #     if line[-1] == "Q":
    #         line = line + next_line[j]
    #     else:
    #         ans = min(ans, len(line))
    #         break
    # 1 способ не полностью проверяет все случаи
    for j in range(len(next_line)):
        if next_line[j] != "Q":
            ans = min(ans, len(line) + j + 1)
            break
    else:
        ans = min(ans, len(line) + len(next_line) + 1)
print(ans)
