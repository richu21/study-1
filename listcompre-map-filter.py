x = [(x,y) for x in range(10) for y in range(10) if x%2== 0 if y%2==1]
y = ["Even" + str(num) if num%2==0 else "Odd" + str(num) for num in range(20) ]
print(y)

t = [1,2,3,4]
t2= [5,6,7,8]

m = map(lambda x,y : x*y,t,t2)
print(list(m))

p = filter(lambda x :x%2 == 0,t)
print(list(p))