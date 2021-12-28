# 三元运算符(条件运算符)
# 语句1 if 条件表达式 else 语句2

# print("你好")if False else print("Hello")

a = 10
b = 50
c = 15
# print("a的值更大") if a > b else print("b的值更大")

# 获取a、b之间较大值
max = a if a>b else b
# print(max)

# # 练习获取abc中最大值
# max = a if a>b else b
# max = max if max>c else c

max = a if (a>b and a>c) else (b if b>c else c)
print(max)
