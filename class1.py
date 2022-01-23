class cars :
    "test class cars"
    colour = 'white'
    def __init__(self,company,model,power) :
        self.company =  company
        self.model = model
        self.power = power

    def driving(self) :
        print("Drive mode onn")

class electriccars(cars) :
    "new concept"
    def __init__(self,company,model,power,battery) :
        self.battery = battery
        super().__init__(company,model,power)
        self.driving()
    
    
        

#test with super battery

c1 = electriccars('maruthi','swift',90,12000)

print(c1.model)

# print(cars.__bases__)





