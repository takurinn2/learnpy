# 高阶函数
# 接受函数作为参数，或将函数作为返回值的函数是高阶函数
# 当我们使用一个函数作为参数时，实际上是将代码传递进目标函数

# 创建列表
l = [1,2,3,4,5,6,7,8,9,10]

# 定义一个函数
#   可以将制定列表中的所有偶数，保存到一个新的列表中返回

    # 定义一个函数，用来检查一个任意数字是否是偶数
def fn2(i):
    if i % 2 == 0:
        return True
    return False

# 函数用来检查数字是否大于5
def fn3(i):
    if i > 5:
        return True
    return False

def fn(func,lst):


    '''
        fn()函数可以将制定列表中的所有偶数获取出来，并保存到一个新的列表中返回

        参数：
            lst 要筛选的列表
    '''
    # 创建新列表
    new_list = []

    # 列表筛选
    for n in lst:
        if func(n):
            new_list.append(n)
        # if n % 2 == 0:
            # new_list.append(n)
    return new_list

# def fn4(i):
#     if i % 3 ==0:
#         return True
#     return False

def fn4(i):
    return i % 3 == 0

lambda i : i % 3 == 0

# print(fn(fn4,l))
# print(l)




# filter()
# filter()过滤器，可以从序列中过滤出符合条件的元素，保存到一个新的序列中
# 参数:
#   1.函数，根据该函数来过滤序列(可迭代的结构)
#   2.需要过滤的序列(可迭代的结构)
# 返回值:
#   过滤后的新序列(可迭代结构)

# fn4时是作为参数传递进filter()函数中
# 而fn4实际上只有一个作用，就是作为filter()的参数
# filter()调用完毕以后，fn4就已经没有作用了
# 匿名函数 lambda 函数表达式(语法糖)
#   lambda函数表达式专门用来创建一些简单的函数，他是函数创建的一种方式
#   语法: lambda 参数列表 : 返回值
# 匿名函数一般都是作为参数使用，其他地方一般不会使用

def fn5(a,b):
    return a + b
# print(fn5(123,456))

# (lambda a,b : a + b)(123,456)
# 也可以将匿名函数复制给一个变量
fn6 = lambda a,b : a + b
print(fn6(123,456))

r = filter(lambda i : i % 3 == 0 ,l)
print(list(r))
# print(list(filter(fn4,l)))
# r = filter(fn4,l)
# print(list(r))


# map()函数可以对可迭代对象中的所有元素做指定的操作，然后将其添加到新的对象中返回
l = [1,2,3,4,5,6,7,8,9,10]
r = map(lambda i : i ** 2 , l)

print(list(r))

