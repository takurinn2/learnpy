# 列表的方法
my_list = ['001','002','003','004']
print('原列表:',my_list)


# append(x)
# my_list[4] = '005'
my_list.append('005')#向列表最后添加一个元素
print('修改1',my_list)

# inset()
# 向列表的指定位置插入一个元素
# 参数：
# 1.要插入的位置
# 2.要插入的元素
my_list.insert(3,'003.5')
print('修改2',my_list)

# extend()
# 使用新的序列来扩展当前序列
# 需要一个序列作为参数
my_list.extend(['010','011'])
print('修改3',my_list)



# clear()
# 清空序列
# my_list.clear()

# pop()
# 根据索引删除并返回被删除元素
result = my_list.pop(2)#删除索引为2的元素
print('修改4',my_list)
print('result =',result)

# remove()
# 删除指定元素(值)，如果元素有多个，只会删除第一个
my_list.remove('005')
print('修改4',my_list)



# reverse()
# 反转列表
my_list.reverse()
print('修改5',my_list)

# sort()
# 用来对列表中的元素进行排序
my_list2 = list('asdjhksahjkabfka')
# my_list2.sort()#默认升序
my_list2.sort(reverse = True)
print(my_list2)