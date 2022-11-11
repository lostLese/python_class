
# question 1
name = input("请输入一个学生姓名\n")
name = name.strip(" ")

n = len(name)
name1 = ""
for i in range(0,n-1):
    name1 += name[i] + "-"
name1 += name[n-1]

print(name1.center(20,"*"))

#question 1 the second way
name = input("请输入一个学生姓名\n")
name = name.strip(" ")
name = list(name)
sign = "-"
name = sign.join(name)
print(name.center(20,"*"))

# question 2
words = input("请输入一个英文语句，注意不要使用其他符号\n")
wordsArray = words.split(" ")
sign = "*"
words1 = sign.join(wordsArray)
print(words1)
print(len(wordsArray))

# question 3
name = input("请输入姓名：")
id = input("请输入身份证号:")
print(name.center(30,"*"))
print("出生日期："+id[6:10]+"年"+id[10:12]+"月"+id[12:14]+"日")



