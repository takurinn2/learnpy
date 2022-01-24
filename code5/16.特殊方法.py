# 特殊方法也称为magic
# 特殊方法都是使用__开头和结尾
# 定义一个Person类
class Person(object):
    '''
        人类
    '''
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    
    # __str__()这个特殊方法会在尝试将对象转换为字符串的时候调用
    # 他的作用可以用来指定对象转换为字符串的结果
    def __str__(self) :
        return 'Person[name=%s , age=%d]'%(self.name,self.age)
    
    # __repr()这个特殊方法会在对当前对象使用repr()函数时调用
    # 他的作用是指定对象在  '交互模式'  中直接输出结果
    def __repr__(self) :
        return 'hello'

    # object.__lt__(self,other)小于
    # object.__le__(self,other)小于等于
    # object.__eq__(self,other)等于
    # object.__ne__(self,other)不等于
    # object.__gt__(self,other)大于
    # object.__ge__(self,other)大于等于

    # __gt__会在对象做大于比较的时候调用，该方法的返回值将会作为比较的结果
    # 它需要两个参数，一个self表示当前对象，other表示和当前对象比较的对象
    # self > other
    def __gt__(self , other):
        return self.age > other.age

    # __len__()获取对象长度

    # object.__bool__(self)
    # 可以通过bool来指定对象转换为布尔值的情况
    def __bool__(self):
        return self.age > 17




# 创建两个Person类的实例
p1 = Person('孙悟空',10)
p2 = Person('猪八戒',28)

# 当我们打印一个对象时，实际上打印的是对象中的特殊方法__str__()的返回值
# print(p1)   #<__main__.Person object at 0x7fbcc00895e0>
# print(p1)
# print(p2)

# print(repr(p1))

# t = 1,2,3
# print(t)

# print(p1 > p2)
# print(p2 > p1)

# print(bool(p1))

if p1 :
    print(p1.name,'已经成年了')
else :
    print(p1.name,'还未成年')


