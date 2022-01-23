class mob :
    def __init__(self,cmpny,type,os) :
        self.cmpny = cmpny
        self.type = type
        self.os = os
    
    @classmethod
    def fromosid(cls,cmpny,type,osid) :
        os = cls.osname(osid)
        return cls(cmpny,type,os)

    @staticmethod
    def osname(osid) :
        if osid == 1 :
            os = "Android" 
        elif osid == 2 :
            os = "IOS"
        else :
            os ="Blackberry os"
        return os


m1 = mob("samsung","Npte 10","android")
print(m1.os)

m2 =mob.fromosid("Appe","1phone 12 pro",2)
print(m2.__dict__)




