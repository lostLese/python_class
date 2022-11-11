# def draw3(N):
#     for i in range(N):
#         print(" "*(40-i) +"*"*(i*2+1))
#
# draw3(30)
# def aa(n,*sd):
#     print(sd[1])
#
# aa(1,'s','ds')

import random
import turtle
# turtle.speed(0)
# turtle.shape("turtle")
# print(turtle.getshapes())
#
# for i in range(random.randint(1, 299)):
#     ln = random.randint(1, 7)
#     r = random.uniform(20.0, 100.0)
#     color = random.choice(["yellow", "green", "red", "blue", "gray", "black", "purple"])
#     turtle.color(color)
#     turtle.fillcolor(color)
#     turtle.pendown()
#     turtle.begin_fill()
#     turtle.circle(r, 360, ln)
#     turtle.end_fill()
#     turtle.penup()
# turtle.done()

# import random
# import turtle
#
# def drawPartten(ln,r,*color):
#     turtle.speed(0)
#     turtle.hideturtle()
#     turtle.fillcolor(color[0])
#     turtle.pendown()
#     turtle.begin_fill()
#     turtle.circle(r, 360, ln)
#     turtle.end_fill()
#     turtle.penup()
#
# drawPartten(4,20,'red')
import random
import turtle

# def drawPartten(ln,r,*color):
#     turtle.colormode(255)
#     turtle.speed(0)
#     turtle.hideturtle()
#     turtle.fillcolor(color[0],color[1],color[2])
#     turtle.pendown()
#     turtle.begin_fill()
#     turtle.circle(r, 360, ln)
#     turtle.end_fill()
#     turtle.penup()
#
# drawPartten(4,20,255,0,0)

# import turtle
#
# def drawPartten():
#     ln = random.randint(1, 8)
#     r = random.uniform(20.0,100.0)
#     color1 = random.randint(0,255)
#     color2 = random.randint(0, 255)
#     color3 = random.randint(0, 255)
#     turtle.colormode(255)
#     turtle.speed(0)
#     turtle.hideturtle()
#     turtle.fillcolor(color1, color2, color3)
#     turtle.pendown()
#     turtle.begin_fill()
#     turtle.circle(r, 360, ln)
#     turtle.end_fill()
#     turtle.penup()
#
# drawPartten()

import random
import turtle

# def drawPartten(ln,r,*color):
#     turtle.pencolor('red')
#     turtle.colormode(255)
#     turtle.speed(0)
#     turtle.hideturtle()
#     turtle.fillcolor(color[0],color[1],color[2])
#     turtle.pendown()
#     turtle.begin_fill()
#     turtle.circle(r, 360, ln)
#     turtle.end_fill()
#     turtle.penup()
#
# drawPartten(4,20,0,255,0)

import random
import turtle
 
def drawPartten(ln,r,*color):
    turtle.pencolor('red')
    turtle.colormode(255)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.fillcolor(color[0],color[1],color[2])
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(r, 360, ln)
    turtle.end_fill()
    turtle.penup()

n = random.randint(0, 10)
for i in range(1,n):
    drawPartten(4,20,0,255,0)
