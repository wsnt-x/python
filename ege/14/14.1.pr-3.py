a = 5*216**3031 + 4*36**3042 - 3*6**3053 - 3064
sumi=0
while a:
    sumi+=a%6
    a//=6
print(sumi)