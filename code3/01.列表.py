# 列表(list)
# list是python中的一个对象
# list中可以保存多个 有序 的数据
# 列表的创建，列表的操作
# 通过[]来创建列表

my_list = []#创建空列表
my_list = [10,20,30,40,50]#里面有五个元素
my_list = [10,'hello',True,None,[1,2,3],print]
print(my_list)

# 可以通过索引(index)来获取列表中的元素
# 索引是从0开始的整数
print(my_list[1])

# 获取列表的长度
print(len(my_list))
# 一共6个元素，输出6