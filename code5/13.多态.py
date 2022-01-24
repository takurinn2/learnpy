# 多态是面向对象的三大特征之一
# 多种形态
# 一个对象可以以不同的形态去呈现

# 定义两个类
class A():
    def __init__(self,name):
        self._name = name

    @property
    def name(self) :
        return self._name
    
    @name.setter
    def name(self,name) :
        self._name = name

class B():
    def __init__(self,name):
        self._name = name

    def __len__(self):
        return 10

    @property
    def name(self) :
        return self._name
    
    @name.setter
    def name(self,name) :
        self._name = name
        
class C:
    pass
a = A('孙悟空')
b = B('猪八戒')
c = C()

# print(b.name)
# 定义一个函数
# 对于say_hello()这个函数来说，只要对象含有name属性，他就可以作为参数传递
    # 这个函数不会考虑对象的类型，只要有name属性即可
def say_hello(obj):
    print('你好%s'%obj.name)

# 在say_hello_2()中做了一个类型检查，也就是只有obj是A类型的对象时，才可以正常使用，
    # 其他类型的对象都无法使用该函数，这个函数就违反了多态
# 违反了多态的函数，只适用于一种类型的对象，无法处理其他类型的对象，这样导致函数的适应性特别差
# 注意,像isinstance()这种函数，在开发中一般是不会使用的!
def say_hello_2(obj) :
    if isinstance(obj , A):
        print('你好%s'%obj.name)

# say_hello(b)
# say_hello_2(b)

# 鸭子类型
# 如果一个东西，走路像鸭子，叫声像鸭子，那么它就是鸭子

# len()
# 之所以一个对象能通过len()来获取长度，是因为对象中具有一个特殊方法__len__
# 只要对象中具有__len__特殊方法就可以通过len()来获取长度
l = [1,2,3]
s = 'hello'
# print(len(l))
# print(len(s))
print(len(b))
print(len(c))


# 面向对象的三大特征:
    # 封装
        # 确保对象中数据安全
    # 继承
        # 保证了对象的可扩展性
    # 多态
        # 保证了程序的灵活性