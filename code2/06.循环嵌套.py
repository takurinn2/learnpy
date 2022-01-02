# 乘法表练习
a = 1

while a < 10:
    i = 0
    while i < a:
        i += 1
        print(f"{i} * {a} = {a*i} ",end="")        
    print()
    a += 1
