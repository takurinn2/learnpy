stus = ['sx1','sx2','sx3','sx4','sx5','sx6','sx3','sx7','sx3']
# + 和 *

# + 可以将两个列表拼接为一个列表
my_list = [1,2,3] + [4,5,6]
#  * 重复指定次数
my_list = [1,1,2,3] * 3
print(my_list)

# in 和 not in
# in用来检查指定元素是否存在列表中
# 如果在返回True，否则返回False
# not in原理类似
print('sx1' in stus)

# len()
# min()
# max()
arr = [10,2,532,42,111,5]
print(min(arr),max(arr))


# 两个方法(method),方法和函数基本上一样，方法必须通过 对象.方法() 的形式调用

# xxx.print()
# s.index() 获取指定元素在列表中的第一次出现的索引
# index()第二个参数表示查找的起始位置,第三个参数表示查找的结束位置
print(stus.index('sx3',4,8))

# s.count()
# 统计元素在列表中出现的次数
print(stus.count('sx3'))
