from collections import defaultdict
my_list=[13.13,'this is my string',13]
d=defaultdict(list)
for x in my_list:
    d[type(x)].append(x)
    fl= d[float]
    st= d[str]
    inte= d[int]
print(fl)
print(st)
print(inte)
