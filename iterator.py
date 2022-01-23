class test : 
    def __init__(self,limit) :
        self.limit = limit
    def __iter__(self) :
        self.num = 1
        # self.limit = self.limit
        return self

    def __next__(self) : 
        x= self.num
        if x < self.limit : 
            self.num += 1
            return x 
        else : 
            raise StopIteration

t = test(15)
m = iter(t)
for x in m :
    print(x)

