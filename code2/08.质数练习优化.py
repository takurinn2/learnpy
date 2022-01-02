# 引入time模块
from time import *

# 优化前:10000个数6.29s
# 第一次优化:10000个数0.78s / 100k个数65.82s
# 第二次优化:100k个数0.62s
begin = time()

i = 2
while i <= 100000:
    flag = True
    j = 2
    while j <= i ** 0.5: #第二次循环更改条件直到i**0.5
        if i % j == 0:
            flag = False
            break #优化第一次
        j += 1
    if flag :
        print(i)
    i += 1
end = time()
print('程序花费了:',end - begin ,"秒")