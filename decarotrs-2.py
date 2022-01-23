def dec(func) :
    def wrapper(name) :
        print("inaside wrapper--",name )
        func(name)
    return wrapper


@dec
def msg(name) :
    print("inside old func---",name)

if __name__ =="__main__" :
    msg("richu")