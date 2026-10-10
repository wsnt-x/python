with open(r"files/24_19254.txt") as f:
    data = f.readline()

# data = "**FSRQ****FSRQ***FSRQ*FSRQ***"

data = data.replace("FSRQ","*** ***")
data = data.split()

ans = 0
for i in range(len(data) - 80):
    ans = max(ans, len("".join(data[i : i + 81]).replace("******","FSRQ")))
print(ans)
