class Rectangle :
    '''
        表示矩形的类
    '''
    def __init__(self , width , height) :
        self.hidden_width = width
        self.hidden_height = height
    
    def get_width(self) :
        return self.hidden_width
    
    def get_height(self) :
        return self.hidden_height
    
    def set_width(self , width) :
        self.hidden_width = width
    
    def set_height(self , height) :
        self.hidden_height = height
    
    def get_area(self) :
        return self.hidden_height * self.hidden_width

# r = Rectangle(5,2)
# r.get_width(10)
# r.get_height(20)

# print(r.get_area())

# 可以为对象的属性使用双下划线开头，__xxx
# 双下划线开头的属性，是对象的隐藏属性，只能在类的内部访问
# 其实隐藏属性只不过是Python自动为属性改了一个名字
    # 实际上是将名字修改为了，__类名__属性名 比如 __name -> _Person__name
class Person :
    def __init__(self , name) -> None:
        self.__name = name
    
    def get_name(self) :
        return self.__name

    def set_name(self , name) :
        self.__name = name
    
p = Person('孙悟空')

p.hidden_name = '猪八戒'

# p.__name = '111'
# print(p.__name)
# print(p._Person__name)
p._Person__name = '猪八戒'
# print(p.get_name())



# 使用__开头的属性，实际上依然可以在外部访问，所以这种方式我们一半不用
    # 一般我们会将一些似有属性(不希望被外部访问的属性)以_开头
    # 一般情况下，使用_开头的属性都是私有的属性，没有特殊需要不要修改私有属性

class Person :
    def __init__(self , name) -> None:
        self._name = name
    
    def get_name(self) :
        return self._name

    def set_name(self , name) :
        self._name = name

p = Person('abc')

print(p._name)