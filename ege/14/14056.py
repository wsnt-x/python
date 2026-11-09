a = 5*1296**2021 - 4*216**2022 + 3*36**2023 - 2*6**2024 - 2025
b=[]
k=0
while a:
    b.append(a%36)
    a//=36
for i in b:
    if i%2==0:
        k+=1
print(k)