# sort()
# 该方法用来对列表中的元素进行排序
# sort()方法默认是直接比较列表中的元素的大小
# 在 sort()中可以接受关键字参数 ， key
#   key需要一个函数作为参数,当设置了函数作为参数
#   每次都会以列表中的一个元素作为参数来调用函数，并且使用函数的返回值来比较元素的大小
l = ['bb','aaaa','c','dddd','fff']
# l.sort(key=len)

l = [2,5,'1',3,'6','4']
l.sort(key=int)
print(l)

# sorted()
# 这个函数和sort()的用法基本一致，但是sorted()可以对任意序列进行排序
#   并且使用sorted()进行排序不会影响原来的对象，而是返回一个新对象

l = [2,5,'1',3,'6','4']
print('排序浅:',l)
new_l = sorted(l,key=int)
print(new_l)
print('排序后:',l)
