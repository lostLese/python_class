import random
import turtle
turtle.speed(0)
turtle.shape("turtle")
print(turtle.getshapes())

for i in range(random.randint(1, 299)):
    ln = random.randint(1, 7)
    r = random.uniform(20.0, 100.0)
    color = random.choice(["yellow", "green", "red", "blue", "gray", "black", "purple"])
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(r, 360, ln)
    turtle.end_fill()
    turtle.penup()
turtle.done()
