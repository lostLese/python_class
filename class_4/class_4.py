# 循环控制
# 死循环 Ctrl + c
import math as t
import turtle
# print(math.inf)
# print(-math.inf)
# print(1 if math.inf > 1 else 0)

# a = input('请输入字符串')
# n = eval(input("输入数字"))
#
# for j in range(1,n+1):
#     sum = 0
#     for i in range(1, (int(j/2)+1)):
#         if j % i == 0:
#             sum += i
#     if sum == j:
#         print(j)
#
# # py 库
# import numpy as np
# import matplotlib.pyplot as plt
# print(t.sin(30))
# #
# turtle.setup(3000,2000)
# for i in range(4):
#     turtle.right(90)
#     turtle.back(20)
#     turtle.forward(50)
# #
# #
# turtle.circle(100,210,6)
# turtle.circle(100,360,4)
# for i in range(4):
#     turtle(10+10*i, 360, 6)
# turtle.done()


turtle.left(90)
while True:
    turtle.circle(30, 180)
    turtle.right(180)
    turtle.circle(30, -180)
    turtle.right(180)
turtle.done()

