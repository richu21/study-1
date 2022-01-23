class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        "This function returns all combinations of one ingredient and one topping"
        try : 
            templist=[]
            for incre in self.ingredients:
                for topp in self.toppings:
                    templist.append([incre,topp])
            return templist
            
        except Exception as ex :
            print(ex)

# Input section
machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce",'Orange sprinkles', 'Oreos'])
print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]