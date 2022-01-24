class Person :
    def __init__(self,name,age) -> None:
        self._name = name
        self._age = age
    
    # property装饰器，用来将一个get方法，转换为对象的属性
    # 添加微property装饰器之后，我们可以像调用属性一样使用get方法
    # 使用property装饰的方法，必须和属性名一样的
    @property
    def name(self) :
        print('get方法执行了')
        return self._name

    # setter方法的装饰器:@属性名.setter
    @name.setter
    def name(self , name) :
        print('setter方法调用了')
        self._name = name

    @property
    def age(self) :
        return self._age
    
    @age.setter
    def age(self , age) :
        self._age = age

p = Person('猪八戒')

p.name = '孙悟空'
print(p.name)