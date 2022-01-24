# 可以在模块中定义变量，在模块中定义的变量，在引入模块后，可以直接使用
a = 10
b = 20

# 添加了_的变脸，只能在模块内部访问
# 再通过import *引入时，不会引入_开头的变量
_c = 30

# 可以在模块中定义函数，同样可以通过模块访问到
def test():
    print('test')

def test2():
    print('test2')


# 也可以定义类
class Person:
    def __init__(self,name) -> None:
        self.name = name

# 编写测试代码,这部分代码，只有当前文件作为主模块的时候才需要执行
    # 而当模块被其他模块引入时，不需要执行，此时我们要检查当前模块是否是主模块
if __name__ == '__main__':
    test()
    test2()
    p = Person(123)
    print(p.name)