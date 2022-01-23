class mobile :
    def __init__(self,ostype,device) :
        self.ostype = ostype
        self.device = device

    @classmethod
    def osname(cls,ostype,device) :
        if ostype == 1:
            ostype = "Android"
        elif ostype == 2 :
            ostype = "Ios"
        elif ostype == 3 :
            ostype = "Windows"
        elif ostype == 4 :
            ostype = "Symbian"
        mobile.msg(device)
        return cls(ostype,device)
    
    @staticmethod
    def msg(device) :
        print("---: "+str(device))

m1 = mobile.osname(2,'iphone 12')
print(m1.ostype)



