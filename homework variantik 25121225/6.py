from turtle import *
screensize(2500, 2500)
k = 30
tracer(0)
pensize(15)

fd(5 * k)
rt(60)
for i in range(6):
    fd(23 * k)
    rt(45)
    fd(17 * k)
    rt(135)
lt(90)
fd(7 * k)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(5, "red")
done()