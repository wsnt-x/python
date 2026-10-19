from turtle import *

tracer(0)
screensize(10000,10000)
r = 10
lt(90)

for i in range(2):
    fd(10*r)
    rt(90)
    fd(20*r)
    rt(90)
up()
fd(3*r)
rt(90)
fd(7*r)
lt(90)
down()
for i in range(2):
    fd(70*r)
    rt(90)
    fd(90*r)
    rt(90)

for x in range(7,21):
    for y in range(3,11):
        teleport(x*r,y*r)
        dot(3,'red')

update()
done()