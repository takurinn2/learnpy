# 逻辑运算符
# not   非
# and   与
# or    或

a = 1
a = not a
print(a)#False
# 短路运算

# 非布尔值的逻辑运算
#   当我们对非布尔值进行与或运算时，Python会将其当作布尔值运算，最终会返回原值

result = 1 and 2    #2
result = 1 and 0    #0
print(result)