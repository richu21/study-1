
def decaratorfn(func) :
    def wrapper(lst) :
        lst.append(2)
        func(lst)
    
    return wrapper

@decaratorfn
def msg(lst) :
    print("inside main")
    lst.append(1)


lst= list()
t = msg(lst)
print(lst)