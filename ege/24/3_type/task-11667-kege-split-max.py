with open(r"files/24_11667.txt") as f:
    data = f.readline()

# data = "***INFINITY****INFINITY****INFINITY**"

data = data.replace("INFINITY", "####### #######")
data = data.split()

ans = 0
for i in range(len(data) - 1000):
    ans = max(ans, len("".join(data[i : i + 1001]).replace("##############","INFINITY")))
print(ans)
