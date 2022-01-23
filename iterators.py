class counter :
    def __init__(self,start,stop) :
        self.start = start 
        self.stop = stop 
        self.count = start

    def __iter__(self) :
        print("hiiii")
        return self

    def __next__(self) :
        if self.count <= self.stop :
            t = self.count
            self.count += 2
            return t
        else :
            raise StopIteration("--Ended--")

t=counter(2,15)
print(next(t))
print(next(t))





