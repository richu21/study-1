t1 = [1,2,3]
t2 = t1
t3 = t1.copy()
t1.append(5)
t1.pop(2)
print("t1 : " + str(t1))
print("t2 : " + str(t2))
print("t3 : " + str(t3))