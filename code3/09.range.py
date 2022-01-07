# range()是一个函数，可以用来生成一个自然数的序列
r = range(5)    #生成[0,1,2,3,4]
r = range(2,10,2)
r = range(10,0,-1)
# 函数需要三个参数
# 1.起始位置(默认是0)
# 2.结束位置
# 3.步长(默认1)

# print(list(r))

# 通过range()可以创建一个指定次数的for循环
# for()循环除了创建方式意外，其余的都和while一样
# else break continue都可以在for循环使用

n = 1
for i in range(20) :
    print(n)
    n += 1

for s in 'hello' :
    print(s)