from re import finditer

with open(r'files/24_17563.txt') as file:
    data = file.readline()

# data = '898-0-988*987*08798-9789-9877-987'

num = '([7-9][07-9]*)'
pattern = rf'({num}[\*-])+{num}'

matches = [match.group() for match in finditer(pattern,data)]

print(len(max(matches,key=len)))
