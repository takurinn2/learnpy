# 创建字典
# 使用{}
# 语法:{k1:v1,k2:v2,k3:v3}

# 使用dict()函数来创建字典
d = dict(name='swk',age=18,gender='男')

# 也可以将一个包含有双值子序列转换为字典
# 双值序列，序列中只有两个值，[1,2]('a',3)'ab'
# 子序列，如果序列中的元素也是序列，那么我们就称这个元素为子序列
# [(1,2),(3,5)]
d = dict([('name','swf'),('age','18')])
# print(d,type(d))

# len()获取字典中键值对的个数
# print(len(d))

# in 检查字典中是否有指定的键
# not in 检查字典中是否不包含指定的键
# print('hello' in d)

# 获取字典中的值
# 语法:d[key]
# print(d['name'])

# get(key,[default])，该方法用来根据键获取字典中的值
#   如果获取的键在字典中不存在，不会报错，会返回None
#       也可以指定一个默认值，来作为第二个参数，这样获取不到值时，会返回默认值
# print(d.get('name'))
print(d.get('hello','默认值'))

# 修改字典
# d[key] = value
# 如果key存在则修改，不存在则添加
d['name'] = '你爹'
d['address'] = '家里'
# print(d)

# setdefault(key[,default])可以用来想字典中添加key-value
# 如果key已经存在于字典中，则返回key的值，不会对字典做任何操作
# 如果key不存在，则向字典中添加这个key,并设置value

result = d.setdefault('name','猪八戒')
result = d.setdefault('hello','猪八戒')
# print('result =',result)
# print(d)

# update([other])
# 将其他的字典中的key-value添加到当前字典中
# 如果有重复的key，则后边的会替换掉当前的
d = {'a':1,'b':2,'c':3}
d2 = {'d':4,'e':5,'f':6,'a':7}
d.update(d2)
print(d)

# 删除，可以使用del来删除字典中的key-value
del d['a']
del d['b']
print(d)

# popitem()
# 随机删除字典中的一个键值对，一般都会删除最后一个键值对
# 删除之后，它会将删除的key-value作为返回值返回
# 返回的是一个元祖，元祖中有两个元素，第一个元素是删除的key，第二个是value
# 当使用一个popitem()删除空字典时，会抛出异常
# d.popitem()
# result = d.popitem()
# print('result =',result)
# print(d)

# result = d.popitem()
# result = d.popitem()
# result = d.popitem()


# pop(key[, default])
# 根据key删除字典中的key-value
# 删除不存在的key会报错
#   指定默认值，会返回默认值
result = d.pop('d')
result = d.pop('z','指定默认值')
print('result =',result)
# print(d)

# clear()用来清空字典
d.clear()
# print(d)

# copy()
# 用来对字典进行浅复制
# 复制以后的对象是独立的，id不一样
# 浅复制会复制对象内部的值，如果值也是一个可变对象，这个可变对象不会被复制
d = {'a':1,'b':2,'c':3}
d2 = d.copy()
# d2['a'] = 10

d = {'a':{'name':'suk','age':18},'b':2,'c':3}
d2 = d.copy()
d2['a']['name'] = '猪'


print('d =',d ,id(d))
print('d2 =',d2 ,id(d2))
