# break可以用来立即退出循环语句
# continue可以跳过当次循环

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1
# else :
#         print('循环结束')

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
else :
    print('循环结束')