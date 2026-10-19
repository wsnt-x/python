from turtle import *

tracer(0)
screensize(10000,10000)
r = 10
lt(90)

for _ in 'abc':
    fd(39*r)
    rt(90)
    fd(48*r)
    rt(90)
up()
fd(27*r)
rt(90)
fd(24*r)
lt(90)
down()
for _ in 'abc':
    fd(29*r)
    rt(90)
    bk(18*r)
    rt(90)

for x in range(24,43):
    for y in range(0,13):
        teleport(x*r,y*r)
        dot(3,'red')

print(39*48 + 29*18 - 18*12)
update()
done()