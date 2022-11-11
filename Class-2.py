# 2022/9/16
a = " dadada "
a = a.strip(" ")
print(a)
print("*"*1000)


for i in range(1,6):
    print(" "*(5-i),"*"*(2*i-1),end="\n")

a = 3.1415926
print("{:30.2}".format(a))
# "{}" 相当于占位符 "{1} {3} {2}".format(1,2,3) sys 1 3 2
print("{}+{}={}".format(3,2,3+2))
print("{2}+{1}={0}".format(3,2,3+2))


print("{0:b} {0:c} {0:d} {0:o} {0:x} {0:X}".format(1000))
# print("{} {} {} {}".format(3.1415926))

# 表英文限定的逗号隔开的内容
# print("%2.2f %%" % (a*10))
# n = eval(input("输入单个数字"))
#
# a = 0
n = eval(input("输入单个数字"))
a = n
k = n
for i in range(1, 3):
    a += pow(10, i)*n
    k += a
print("{0} + {0}{0} + {0}{0}{0} = {1}".format(n, k))

import math
print(math.pi)
print("{:1.20}".format(math.pi))


n = eval(input("输入范围数字"))
s = "{:1."+str(n)+"}"
print(s.format(math.pi))
print("{0:-^30.{1}f}".format(math.pi, n))
s = "1232144314"
print(s[::2])
print(s[::-2])

print(s[-4:])
print(s[:])

str = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
x = 3
n =3
for i in range(3):
    print(str[i::n])