# 元祖 tuple
# 元祖是一个不可变的序列
# 它的操作方式基本上和列表是一致的
# 操作元祖时，当成不可变列表
# 我们希望数据不被改变时，用元祖，其他情况都用列表

# 创建元祖
# 使用()来创建元祖
my_tuple = ()#一个空元祖
# print(type(my_tuple))

my_tuple = (1,2,3,4)
print(my_tuple)
print(my_tuple[3])

# 元祖的解包(解构)
# 将元祖的每一个元素都赋值给一个变量
a,b,c,d = my_tuple
print('a =',a)
print('b =',b)
print('c =',c)
print('d =',d)

a = 100
b = 300
print(a,b)
# 交换a和b的值，可以利用元祖的解包
a,b = b,a
print(a,b)

my_tuple = (10,20,30,40,50,60)
# 解包的时候，可以在变量前加*，此变量会获取元祖中所有剩余的元素
a,b,*c = my_tuple
print(a,b)
print('c =',c)