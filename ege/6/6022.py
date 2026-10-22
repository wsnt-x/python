from turtle import *

tracer(0)
screensize(10000, 10000)
r = 10
lt(90)

for i in range(10):
    fd(22 * r)
    rt(90)
    fd(16 * r)
    rt(90)
up()
fd(1 * r)
rt(90)
fd(1 * r)
lt(90)
down()
for i in range(10):
    fd(72 * r)
    rt(90)
    fd(79 * r)
    rt(90)

for x in range(1, 17):
    for y in range(1, 23):
        teleport(x * r, y * r)
        dot(3, 'red')

update()
done()
print(2 * (15 + 21))
