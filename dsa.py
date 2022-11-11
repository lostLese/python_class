import math

m = eval(input("输入起始整数"))
n = eval(input("输入结尾整数"))
c = ""
count = 0
for i in range(m, n + 1):
    t = True
    if i == 1:
       continue
    #     sqrt(i)+1简化求值
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            t = False
            break
    else:
         #  c += str(i)+" "
        count += 1
         # if count % 5 == 0:
            # print(c)
        print(i,end=(" " if count % 5 != 0 else "\n"))
           # c = ""