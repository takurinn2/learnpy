class Animal :
    def run(self):
        print('动物跑')

    def sleep(self):
        print('动物睡觉')

class Dog(Animal) :
    def bark(self) :
        print('狗叫')

    def run(self) :
        print('狗跑')

# 如果子类中和父类同名的方法，则通过子类实例去调用方法时，
    # 会调用子类的方法，而不是父类的方法，这个特点叫做方法的重写(覆盖,override)
# 创建Dog类的实例
# d = Dog()

# d.run()

# 当我们调用一个对象的方法时，
    # 会优先去当前对象中寻找是否具有该方法，如果有则直接调用
    # 如果没有，则去父类，父类的父类
class A():
    def test(self):
        print('AAA')

class B(A):
    def test(self):
        print('BBB')

class C(B):
    def test(self):
        print('CCC')

c = C()
c.test()