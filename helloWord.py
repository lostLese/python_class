# if 5 > 2:
#     print('Hello,World')
#     a = 10
#     print(type(a))
#
# b = ["2","dsa","sd"]
# for x in b:
#     print(x)
#
# #sds
# print('ss'=="ss")
# """
# sdad
# dsa
# dasd
# """
#
# a = "sdadsa"
# i = 0
# for x in a:
#
#     print(a[i])
#     i += 1
#
# a1 = """"
# dsadsad
# sdsadsada
# sadsad
# sdadas
# das
# dsa
# dsa
# dsa
# """
# print(a1)
# print(a1[2:5])
# print(a1[-5:-2])
# print(len(a1))
# print(a1.strip())
# print(a1.upper())
# print(a1.lower())
# print(a1.replace("sda","kkk"))
# #使用eval()函数,将字符串还原为数字类型
# a = eval(input("输入行数"))
# for i in range(1,a+1):
#     print("==")
# name = input("请输入姓名")
# print("你好"+name)
# a = eval(input("输入长"))
# b = eval(input("输入宽"))
# print("面积为"+a*b)

# c = eval(input("输入表达式"))
# print(c)
# x = 2
# print(eval("x*x"))
# print("sd","sd","s",sep="/n")
# a = 123
# b = 133
# c =90
# print("平均分%5.2f"%((a+b+c)/3),"sdda",end="")
# print("平均分%5.2f"%((a+b+c)/3),"sdda",end="")


#选修第一章作业
import keyword
import math
for i in range(1,101):
    print(i)
for i in range(1,101,2):
        print(i)
for i in range(1,101):
    n = int(math.sqrt(i))
    flag = 0
    for j in range(2,n+1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i)

# #格式
# s=3.1415926
# print("{0:-^30,.3f}".format(s))
# #------------3.142-------------
# s1 = input("请输入英文语句")
# str1 = s1.split(" ")
# print(str1[-1],str1[-2],str1[-3],sep="\n")

#标识符
print = 1
a = print
#删除标识符，复用print函数
del print
print(a)

#keyword模块
keyword.kwlist

#elif 等于else if
if 1 > 2:
  print(1>1)
elif 2 < 3:
  print(2>1)

print(1000*"*")

#python,整数没有长度限制，实际取值受限于计算机的内存容量，0x,0b,0o,直接输出
k1 = 0o2
k2 = 0x3
k3 = 0b1
k4 = 5
print()

#尾数问题，二进制无法表达所有的十进制数字

#/ 整数 / 整数  = 浮点数  整数 * 整数 = 整数
#
# #complex 复数类型
# a = eval(input("请输入复数类型"))

#bool类型 False True
a = False
b = True

#单引号 双引号 三个引号
a = '''
dsada
dsada
dsadas
# '''
# print(a)
#
# #上机练习
# r = eval(input("请输入半径"))
# pai = 3.1415926
# c = pai*r*2
# s = r*r*pai
# v = 4/3*r**3*pai
# print("圆周长",'\t',"{:.4f}".format(c))
# print("圆面积",'\t',"{:.4f}".format(s))
# print("球体积",'\t',"{:.4f}".format(v))

# id() type() 注意py先生成数据再让变量名指向它


# "da" in "dadadadada" ;"dsad" * int ;"dsad" + "dDsad"

# x and y; x or y; not x
#
# a = 1
# print(a << 1,a>>1,a&1,a|1,,a^1,a~1)


# a in b , a not in b a is b
a = "5.3"
b = "5.3"
print(a is b)
a = ("dsad爬","c")
b = ("dsad爬","c")
print(id(a),id(b))

# 强制类型转换


# 2020/9/9上机2
s = eval(input("请输入三位数字"))
print(int(math.pow(s//100,2)),int(math.pow(s//10%10,2)),int(math.pow(s%10,2)))

for i in range(1,6):
    print(" "*(5-i),"*"*(2*i-1),end="\n")






