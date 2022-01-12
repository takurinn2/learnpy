# 遍历字典
# keys()    该方法会返回字典的所有的key
# values()  该方法会返回一个序列，序列中保存有字典的所有的值
# items()   该方法会返回字典中所有的项

# keys()
# 通过遍历keys获取所有的键
d = {'name':'你爹','age':18,'gender':'男'}
# print(d.keys())
# for k in d.keys():
#     print(k,d[k])

# values()
# for v in d.values():
#     print(v)

# items()
# 会返回一个序列，序列中包含有双值子序列
# 双值分别的是,key,value
print(d.items())
for k,v in d.items():
    print(k , '=' , v)
