from re import finditer

with open(r"files/24_17641.txt") as file:
    data = file.readline()

num = "([1-9][0-9]*|0)"
pattern = rf"({num}[\*\+])+{num}"

matches = [match.group() for match in finditer(pattern, data)]

ans = 0
for line in matches:
    len_line = len(line)
    if eval(line) == 0:
        ans = max(ans, len_line)
    elif len_line > ans:
        for l in range(len_line - 1):
            if line[l] in "+*" or line[l] == "0" and line[l + 1] in "0123456789":
                continue
            for r in range(len_line - 1, l, -1):
                if line[r] in "*+":
                    continue
                if eval(line[l : r + 1]) == 0:
                    ans = max(ans, r - l + 1)
                    break
print(ans)

##########################################################

from re import finditer

with open(r"files/24_17641.txt") as file:
    data = file.readline()

number = r"(0|[1-9][0-9]*)"
zero_part = rf"({number}\*)*0(\*{number})*"
pattern = rf"{zero_part}(\+{zero_part})*"

matches=[match.group() for match in finditer(pattern,data)]

print(len(max(matches, key = len)))
