def fib(limit,count=0,sum=0) :
    if count <= limit :
        sum += count 
        count += 1
        print(sum)
        fib(limit,count,sum)
    else :
        print("---completed---")

fib(10)