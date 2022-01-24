class A(object):
    def test(self):
        print('AAA')

class B(object):
    def test2(self):
        print('BBB')

# 在Python中是支持多重继承的，也就是我们可以为一个类同时指定多个父类
    # 可以在类名的()后边添加多个类，来实现多重继承
    # 多重继承，会使子类同时拥有多个父类，并且会获取到所有父类中的方法
# 在开发中没有特殊的情况，应该尽量避免使用多重继承，因为会让代码过于复杂
# 如果多个父类中有同名的方法，则会在第一个父类中寻找，前面会覆盖后面
class C(A,B):
    pass

# 类名.__bases__ 这个属性可以用来火气当前类的所有父类
# print(C.__bases__)
# print(B.__bases__)

c = C()
c.test()
c.test2()