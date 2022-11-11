import time as ac
import turtle
turtle.hideturtle()
turtle.setup(800,600)
turtle.speed(0)
turtle.shape("turtle")
turtle.forward(80)
turtle.right(90)
turtle.forward(180)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(180)
turtle.right(90)
turtle.forward(40)
turtle.right(180)
turtle.circle(30, -540)
turtle.right(180)
turtle.circle(30, -540)
turtle.right(180)
turtle.circle(30, -540)
t = 0
s = 0
forwd = 3
color = ["green", "yellow", "red"]
time = [3, 2, 3]
while t != 30:
    if forwd != 3:
        s = s % 3
        forwd += 1
        turtle.fillcolor(color[s])
        turtle.begin_fill()
        turtle.circle(30, -540)
        turtle.end_fill()
        ac.sleep(time[s])
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.circle(30, -360)
        turtle.end_fill()
        turtle.right(180)
        s += 1
    else:
        forwd = 0
        turtle.penup()
        turtle.seth(90)
        turtle.forward(180)
        turtle.seth(180)
        turtle.pendown()
    t += 1
turtle.done()
