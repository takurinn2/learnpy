old = [12,2,'hello',13,1,['hello',12,[1,'2','1',['3','13']]]]
a = list()
b = tuple()
new = []
for b in old:
    set(tuple(b))
