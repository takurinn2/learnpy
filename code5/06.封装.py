# 封装是面向对象的三大特性之一
# 封装指的是隐藏对象中不希望被外部访问到的属性或方法
    # 将对象的属性名，修改为一个外部不知道的名字
# 如何获取(修改)对象中的属性
    # 需要提供一个getter和setter方法使外部可以访问到属性
    # getter 获取对象中的指定属性(get_属性名)
    # setter 用来设置对象的指定属性(set_属性名)
# 使用封装，确实增加了类的定义的复杂程度，但是确保了数据安全性
    # 1.隐藏了属性名，使调用者无法随意的修改对象中的属性
    # 2.增加了getter和setter当大，很好的控制了属性是否是只读的
        # 如果希望属性只读，可以直接去掉setter方法
        # 如果希望属性不被外部访问，去掉getter方法
    # 3.使用setter方法设置属性，可以增加数据的验证，确保数据的值是正确的
    # 4.使用getter方法获取属性，使用setter设置属性
        # 可以在读取属性和修改属性的同时做一些其他的处理
    # 5.使用getter方法可以表示一些计算的属性

class Dog :
    '''
        狗的类
    '''
    def __init__(self , name , age) -> None:
        self.hidden_name = name
        self.hidden_age = age
    
    def say_hello(self) :
        print('大家好我是%s'%self.hidden_name)
    
    def get_name(self) :
        '''
            get_name()用来获取对象的属性
        '''
        # print('用户读取了属性')
        return self.hidden_name

    def set_name(self , name) :
        # print('用户修改了属性')
        self.hidden_name = name

    def get_age(self) :
        return self.hidden_age

    def set_age(self , age) :
        if age > 0 :
            self.hidden_age = age

d = Dog('旺财' , 10)
# d.name = '小黑'

# 调用setter来修改name属性
d.set_name('小黑')
d.set_age(8)

# d.say_hello()
print(d.get_age())