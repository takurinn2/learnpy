# 继承

# 定义一个类 Animal
    # 这个类中需要两个方法:run() sleep()
class Animal :
    def run(self):
        print('动物跑')

    def sleep(self):
        print('动物睡觉')

    # def bark(self) :
    #     print('狗叫')


# class Dog :
#     def run(self):
#         print('动物跑')

#     def sleep(self):
#         print('动物睡觉')

#     def bark(self):
#         print('狗叫')

# 定义一个类 Dog
    # 这个类中需要三个方法: run() sleep() bark()
# 有一个类，能够实现我们需要的大部分功能，但是不能实现全部功能
# 如何实现?
    # 1.直接修改类，在类中添加功能
    # 2.创建一个新的类
    # 3.直接从Animal类中来继承他的属性和方法
        # 继承时面向对象的三大特性之一
        # 在定义类时，可以在类名后的括号中指定当前类的夫类(超类、基类、super)
            # 子类()可以直接继承父类中的所有的属性和方法
# 
# 通过继承符合OCP原则
    # 所以我们通过继承来对一个类进行扩展

class Dog(Animal) :
    def bark(self) :
        print('狗叫')

class Hashiqi(Dog) :
    def chaijia(self):
        print('拆家')

d = Dog()
h = Hashiqi()

# d.run()
# d.sleep()
# d.bark()

# flag = isinstance(d,Dog)
# r = isinstance(d,Animal)
# print(flag,r)

# 在创建时，如果省略了父类，则默认夫类为object
    # object是所有类的夫类，所有类都继承自object
class Person :
    pass

# 检查一个类是否是另一个类的子类
print(issubclass(Dog , Animal))

# isinstance()用来检查一个对象是否是一个类的实例