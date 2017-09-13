name_list = ['practice','for','funcmap']
for n in name_list:
    print(len(n))

name_len = list(map(len,['ni','hao','funPro']))
print(type(name_len),name_len)

def toUpper(item):
    return item.upper()

upper_name = list(map(toUpper,name_list))
print(upper_name)
print('-----------------------------------------')
items = list(range(1,6,1))

squared = []
for i in items:
    squared.append(i**2)
print('squared = ',squared)

squared_new = list(map(lambda x: x**2,items))
print('squared_new = ',squared_new)
