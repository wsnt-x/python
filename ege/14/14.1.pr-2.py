a = 6*144**26 + 11*12**75 - 48
cnt_B = 0
while a:
    if a%12==11:
        cnt_B+=1
    a//=12
print(cnt_B)