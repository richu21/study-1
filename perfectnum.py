n = 100
count = 0
num = 1
t= 1
# while count <= n :
for x in range(2,1000) :
    for y in range(2,int(x/2)+1) :
        if x % y == 0 :
            t=t+y
    if x == t :
        print(t)
    t=1
            # count+=1


