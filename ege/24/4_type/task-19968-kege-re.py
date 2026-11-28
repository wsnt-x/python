from re import finditer

with open(r"files/24_19968.txt") as file:
    data = file.readline()

num = '([1-5][0-5]*|0)'

pattern = rf'({num}[+*])+{num}'

matches = [match.group() for match in finditer(pattern,data)]

print(len(max(matches,key=len)))
