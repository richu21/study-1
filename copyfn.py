import copy

a = [1,2,3]
b= copy.copy(a) #shallowcopy
c= copy.deepcopy(a)
a.append(5)
print(b)
print(c)