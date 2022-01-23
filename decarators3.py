

def dec(func) :
    def inner(lst) :
        lst.append(5)
        func(lst)
        print("decarated")
    return inner

@dec
def a(lst) :
    lst.append(1)


ls = []
a(ls)
print(ls)
