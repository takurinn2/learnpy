# 集合(set)和列表相似
# 不同点
#   1.集合中只能存储不可变对象(hashable)
#   2.集合中存储的对象是无序的
#   3.集合中不能出现重复的元素

# 使用{}创建集合
s = {10,20,1,2,3,4}
# print(s,type(s))

# 使用set()函数来创建集合
s = set()#空集合
s = set([1,2,4,3,-1,-7,42,2])
s = set({'a':1,'b':2,'c':3})#使用set()将字典转换为集合时，只会包含键

# 创建集合
s = {'a','b',1,2,3}
# print(s,type(s))
# print(list(s)[0])

# 使用 in和not in 来检查集合中的元素
print('c' in s)

# 使用len()来获取集合中元素的数量
print(len(s))

# add()向集合中添加元素
s.add(10)
s.add(30)


# update() 将一个集合中的元素添加到当前集合中
s2 = set('hello')
s.update(s2)
s.update((10,20,30,40,50))
s.update({10:'ab',20:'bb',100:'ff',1000:'gf'})
# print(s,type(s))
# {'b', 1, 2, 3, 'a', 'h', 'l', 'e', 40, 100, 10, 1000, 'o', 50, 20, 30}
# pop()随机删除一个集合中的元素
result = s.pop()
s.pop()

# remove()删除集合中的指定元素
s.remove(100)
s.remove(1000)

# clear()清空集合
s.clear()
# print('result =',result)
print(s,type(s))

# copy()对集合进行浅复制