# 返回值，函数执行以后返回的结果
# 可以通过 return 来指定函数的返回值
# 可以直接使用函数的返回值，也可以用变量接收

def sum(*nums) :
    result = 0
    for n in nums :
        result += n
    print(result)

# sum (123,455,432)

# return 后面可以跟任意对象
def fn():
    # return 'Hello'
    def fn2():
        print('hello')
    return fn2
r = fn()#变量接收
# r()
# print(r)
# print(fn())#直接打印

# 如果仅仅写一个return 或者不写ruturn，则相当于return None
def fn2():
    a = 10
    return

# 在函数中return后的代码不会执行
def fn3():
    print('hello')
    return
    print('abc')
# r = fn3()
# print(r)

def fn4():
    for i in range(5):
        if i == 3:
            # break
            # continue
            return # return 用来结束函数
        print(i)
    print('执行完毕')

# fn4()


def sum(*nums) :
    result = 0
    for n in nums :
        result += n
    return result

r = sum(123,456,789)
# print(r)

def fn5():
    return 10
# fn5 和 fn5()的区别
print(fn5)# fn5时函数对象，答应fn实际上是在打印函数对象
print(fn5())# fn5()是在调用函数，打印返回值 10