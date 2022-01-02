stus = ['sx1','sx2','sx3','sx4','sx5','sx6','sx3','sx7','sx3']
print('修改前',stus)
# 修改列表元素
# 直接通过索引修改元素
stus[0] = 'sssxxxx1'
stus[2] = 'sssxxxx3'
# 通过del来删除元素
del stus[8]
print('修改后',stus)

# 通过切片来修改列表
# 在给切片进行赋值时，只能使用序列
stus[0:2] = ['sxx1','sxx2','我是第三个填充']
stus[0:0] = ['牛魔']#向索引为0的位置插入元素
print('修改后2',stus)
# 当设置了步长时，序列中元素的个数必须和切片中元素的个数一致
stus[::2] = ['步长替换']*5
print('修改后3',stus)

# 通过切片删除元素
# del stus[0:2]
# del stus[::2]
stus[1:3] = []
print('修改4',stus)
# 以上操作，只适用于可变序列

s = 'hello'
s = list(s)#改为可变序列
print(s)