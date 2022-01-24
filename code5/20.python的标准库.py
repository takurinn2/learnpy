# 开箱即用
# 为了实现开箱即用的思想，python中为我们提供了一个模块的标准库
# 在这个标准库中，有很多很强大的模块我们可以直接使用
    # 并且标准库会随着python的安装直接安装
# sys模块，它里面提供了一些变量和函数，使我们可以获取到Python解析器的信息
    # 或者通过函数来操作python的解析器
# 引入sys模块
import sys

# pprint 模块他给我们提供了一个方法 pprint() 该方法可以用来对打印的数据进行简单的格式化
import pprint

# sys.argv
# 获取执行代码时，命令行中所包含的参数
# 该属性是一个列表，列表中保存了当前命令的所有参数
# print(sys.argv)

# sys.modules
# 获取当前程序中引入的所有模块
# modules是一个字典，字典的key是模块的名字,字典的值是模块对象
# pprint.pprint(sys.modules)

# sys.path
# ['/Users/choki/pythonlearn/code5',
#  '/Users/choki/opt/anaconda3/lib/python39.zip',
#  '/Users/choki/opt/anaconda3/lib/python3.9',
#  '/Users/choki/opt/anaconda3/lib/python3.9/lib-dynload',
#  '/Users/choki/opt/anaconda3/lib/python3.9/site-packages',
#  '/Users/choki/opt/anaconda3/lib/python3.9/site-packages/aeosa',
#  '/Users/choki/opt/anaconda3/lib/python3.9/site-packages/locket-0.2.1-py3.9.egg']
# 它是一个列表，列表中保存的是模块的搜索路径
# pprint.pprint(sys.path)

# sys.platform
# 表示当前python运行的平台
print(sys.platform)

# sys.exit()
# 函数用来退出程序

sys.exit('程序出现异常')

print('hello')