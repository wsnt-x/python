with open(r"files/24_1273.txt") as f:
    data = f.readline()

data = data.replace("XYZ", "** **").split()

print(len(max(data, key=len)))
