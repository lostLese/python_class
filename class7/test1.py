list1 = [12321, 342, 432, 'dsads', False]
list1 = list(range(1, 5))
list1 = list((1, 2, 3, 4))
list1 = list("sdada")
list1 = list(a * 2 for a in range(1, 5))
# for a in list1:
#     print(a)
# print(list1[-1])
list1.append("dsa")
list1.insert(0, '张三')
for a in list1:
    print(a)


# remove  del 列表[元素序号] del 列表
list1.remove("张三")
del list1[0]
for a in list1:
    print(a)

# list[a:b:num]
list1 = list(a for a in range(19))
list1[10:19:2]=[-1,-1,-1,-1,-1]
for a in list1:
    print(a)
# list 运算
list2 = 2 * list1
list1 = list2 + list1

# list[0:2] = ('dsads')
# list[0:2] = 'dsadada'  被拆分


# 元组
tu1 = (34,43,54,6,5)
tu2 = (2313,'dad',231)
tu3 = ()
# tu4 = (55,)一个元素的元组
tu4 = (55,)
# tu4 = (55)简单变量不是一个元素
tu4 = (55)

# 元组不能修改 列表是可变的
# 元组数据处理效率较高
# 对于可变的批量数据，使用列表存储和处理而对于不变的数据可以使用元组存储

# 对整个元组的赋值，原来元组不要了
tu1 = tu2 + tu3


# sorted 函数


# reverse
# choice
