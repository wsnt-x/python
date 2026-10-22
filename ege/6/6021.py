from turtle import *

tracer(0)
screensize(10000, 10000)
r = 10
lt(90)

for i in range(3):
    fd(7 * r)
    rt(90)
    fd(12 * r)
    rt(90)
up()
fd(4 * r)
rt(90)
fd(6 * r)
lt(90)
down()
for i in range(4):
    fd(83 * r)
    rt(90)
    fd(77 * r)
    rt(90)

for x in range(0, 7):
    for y in range(0, 4):
        teleport(x * r, y * r)
        dot(3, 'red')

update()
done()
