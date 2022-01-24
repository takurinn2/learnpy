class Dog:
    '''
        表示狗的类
    '''
    def __init__(self , name , age , gender , height) :
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
    
    def bark(self) :
        '''
            狗叫的方法
        '''
        print('汪汪汪..')

    def bite(self) :
        '''
            狗咬的方法
        '''
        print('咬!')

    def run(self) :
        '''
            狗跑的方法
        '''
        print('%s在快乐的跑'%self.name)

d = Dog('旺财',8,'male',30)


# 目前我们可以直接通过对象.属性 的方式来修改属性的值，这种方式导致对象中的属性可以随意修改
    # 非常的不安全
# 需要一种方式来增强数据的安全性
    # 1.属性不能随意修改
    # 2.属性不能修改为任意的值
d.name = '阿黄'
d.age = -10
d.run()
print(d.name , d.age , d.gender , d.height)