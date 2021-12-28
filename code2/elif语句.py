# 接收到用户输入的年龄
age = int(input('输入你的年龄'))

# if age >= 18 :
#     print('你已经成年了')
# else :
#     print('???')

if age > 60 :
    print('大于60')
elif age > 17 :
    print('大于18')
elif age > 0 :
    print('大于0')
else :
    print('小于0')