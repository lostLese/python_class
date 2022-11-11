# a = eval(input())
# if a >= 90:
#     print("good")
# elif a >= 80:
#     print("not bad")
# elif a >= 60:
#     print("that's ok")
# else:
#     print("成绩不及格")
#
#
# # 2.b 3.d 4.b
# for i in range(10):
#     print(i)
#
# for i in range(1,11,2):
#     print(i,end="")
#
# x = 5
# if x < 100\
#         and x > 10:
#     print(1)

# 请根据用户输入的2个正整数，输出这2个整数之间的所有素数，输出时，每5个素数为一行。



# s = 1
# n =10
# for f in range(s,n):#这个就是区间范围，在后面调用参数设置参数的话，会给与出来！
#         t = False #设置默认变量t ，t的值为False;不用想太多，只单单认为他是一个变量
#         for j in range(2,f):#在创建一个循环，因为质数2和1都不属于质数，所以从2开始，到f结束。f就是上一个for循环的结果
#             if f%j==0:#f就是我们要求的区间中的数，拿f除以2-f之间的所有数，余数若等于0，则会继续向下执行，如果不是，则不会执行一下的语句
#                 t=True#若余数则是0.则从新赋值t为True
#                 break#跳出循环
#         if t ==False:#素数是不可能执行 t=True这个语句，所以t = False，一直是t = False，用if判断，当t ==False时，执行输出语句#如果t=True，那么就不会执行
#             print(f,end=" ")#f为满足t ==False 输出，end这里是换行，并且“ ” 是保持空格

