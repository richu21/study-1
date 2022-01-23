class myexception(Exception):
    print("hi in my exception")

try :
    x =1 
    if type(1) is int :
        raise myexception("anoter one ")
except myexception as me :
    print(me)
except Exception as ex :
    print("Exception occured")
