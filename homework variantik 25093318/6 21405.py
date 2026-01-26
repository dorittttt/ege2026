from turtle import *

tracer(0)
screensize(500,500)
k = 20
pensize(5)
lt(30*k)
for i in range(3):
    rt(150)
    fd(6*k)
    rt(30)
    fd(12*k)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(5, 'red')

done()