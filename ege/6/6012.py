from turtle import *

tracer(0)
screensize(10000,10000)
r = 10
lt(90)

for _ in 'ab':
    fd(13*r)
    rt(90)
    fd(20*r)
    rt(90)
up()
fd(8*r)
rt(90)
bk(3*r)
lt(90)
down()

for _ in 'ab':
    fd(16*r)
    rt(90)
    fd(8*r)
    rt(90)

for x in range(6):
    for y in range(8,14):
        teleport(x*r,y*r)
        dot(3,'red')

print(14 * 21 + 17 * 9 - 6 * 6)
update()
done()
