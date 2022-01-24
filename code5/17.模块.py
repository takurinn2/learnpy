# 模块(module)
# 模块化，模块化将完整的程序分解为一个一个小的模块
    # 通过将模块组合，来搭建出一个完整的程序
# 不采用模块，统一将所有的代码编写到一个文件中
# 采用模块化，将程序分别编写到多个文件中
    # 模块化的优点：
        # 1.方便开发
        # 2.方便维护
        # 3.模块可以复用

# 在python中一个py文件就是一个模块，要想创建模块实际上就是创建一个python文件
# 注意：模块名要符合标识符的规范

# 在一个模块中引入外部模块
# 1.import 模块名(模块名，就是python文件的名字，注意不要后缀.py)
# 2.import 模块名 as 模块别名
    # 可以引入一个模块多次，但是模块的实例只会创建一个
    # import可以在程序的任意位置调用，一般情况下，import语句都会统一写在程序的开头
    # 在每一个模块内部都有一个__name__属性，通过这个属性可以获取到模块的名字
    # __name__属性值为__main__的模块是主模块，一个程序只会有一个主模块

# import test_module
import test_module as test

# print(test_module)#<module 'test_module' from '/Users/choki/pythonlearn/code5/test_module.py'>
# print(test)

# print(test.__name__)
print(__name__)


