import keyword
# 是不是关键字

import math
import time
# math 库常数

a = math.nan
b = math.nan
print(a == b)
print(math.isclose(4.5, 0.45e1))
print(math.modf(12.45))

t = time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", t))

time.sleep(1)
print(4564)
# 获取cpu级别的时间，纳秒精度 百万分之一
time.perf_counter()


import random
# random.seed()
# random.random()
# print(random.uniform(1.0,20.0)+
# random.randint(1,456)+
# random.randrange(1,10,2))
# print(random.getrandbits(10))
# print(random.choice([4, 'sd', 5]))
# random.shuffle(["dsa", 1, 123])
print(random.randint(0,1))
print(random.randint(0,1))
print(random.randint(0,1))
print(random.randint(0,1))
print(random.randint(0,1))