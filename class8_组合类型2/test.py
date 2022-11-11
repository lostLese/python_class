#
# list1 = ['胡萝卜', '白痴']
# while True:
#     a = input(":")
#     if a.upper() == "END":
#         break
#     list1.append(a)
# print(list1)
# sorted(list1)
# print(list1)

# Dictionary
dic = {1003: 13232, 21312: 1}
print(dic[1003])
dic1= {1003:{"张三":"111","身份证":{"id":"sdad","dsad":"dsads"}}}

print(dic1[1003])
dic2 = dict([[1,2],[2,23],[3,2322]])
print(dic2[2])

# 字符串一定要用'', 防止键和变量无法区分
dic3 = dict("sda"='s',Jusn='s')