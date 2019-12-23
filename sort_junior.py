# sort() accepted an function as key paramter
l = ['bb', 'aaaa', 'c', 'dddddddd', 'fff']
l.sort(key=len)
print(l)


l = [2.5, '1', 3, '6', '4']
l.sort(key=str)
print(l)


