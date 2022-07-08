topclubs = ['mun', 'mci' , 'asn', 'liv', 'che']
print(topclubs)

#使用del删除元素
del topclubs[0]
print(topclubs)

#使用pop删除元素
topclubs.pop()
print(topclubs)

#弹出列表中任何位置的元素
topclubs.pop(0)
print(topclubs)

#根据值删除元素
topclubs.remove('liv')
print(topclubs)