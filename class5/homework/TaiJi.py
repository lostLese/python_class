import turtle
# 40 80 10 60
turtle.speed(0)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(40, 180)
turtle.circle(80, 180)
turtle.circle(40, -180)
turtle.end_fill()
turtle.circle(40, 180)
turtle.circle(80, 180)



turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(10, 360)
turtle.end_fill()
turtle.penup()
turtle.fillcolor("black")
turtle.goto(0, -30)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10, 360)
turtle.end_fill()
turtle.done()