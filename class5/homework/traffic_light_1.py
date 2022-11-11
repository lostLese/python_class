import turtle as t
import time
t.colormode(255)
t.setup(800, 600)
t.hideturtle()

t.dot(100,(255,0,0))
t.setx(100)
t.dot(100, (100, 100, 0))
t.setx(200)
t.dot(100, (0, 100, 0))

for i in range(1,20):
    if i % 3 == 0: # 红灯灭完绿灯亮
        t.setx(0)
        t.dot(100, (100, 100, 0))
        t.setx(200)
        t.dot(100, (255, 0, 0))
    elif i % 3 == 1: # 绿灯灭完黄灯了亮 # 黄灯灭红灯亮
        t.setx(200)
        t.dot(100, (255, 0, 0))
        t.setx(300)
        t.dot(100, (0, 100, 0))
    else:
        t.setx(300)
        t.dot(100, (0, 100, 0))
        t.setx(0)
        t.dot(100, (100, 100, 0))
t.done()