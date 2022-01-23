n = int(input("Enter the limit : "))
space = n-1
for i in range(0,n,2):
    for k in range(space):
        print(" ",end="")
    for p in range(1,i):
        print("*",end = "")
    print("")
    space = space - 1

