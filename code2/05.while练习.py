# 100以内所有奇数和
i = 0
result = 0
while i<100 :
    i += 1
    # 判断是否为奇数
    if i%2 != 0 :
        result = result + i
print(result)

result = 0
# 第二种方法
i = 1
while i<100 :
    result = result + i
    i += 2
print(result)

# 水仙花数
i = 100
while i < 1000 :
    a = i // 100
    b = (i - a * 100) // 10
    c = i - a * 100 - b * 10
    if a**3 + b**3 + c**3 == i :
        print(i)
    i += 1

# 判断质数
num = int(input('输入一个任意的大于1的整数:'))
i = 2
y = True
while i < num:
    if num % i == 0 :
        y = False
    i += 1 
if y :
    print('是质数')
else :
    print('不是是质数')