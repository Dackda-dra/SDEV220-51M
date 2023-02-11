# Drashaun Morrow
#Case study, lists functions and classes
# Utilizing Python version 3.8.10


# create class
class Vehicle():

   def __init__(self):
     self.vehicleType = str(input('Enter vehicle type: '))


   
class automobile(Vehicle):
   def __init__(self):
       Vehicle.__init__(self)
       self.year = int(input("Enter Vehicle year: "))
       self.make = str(input("Enter Vehicle make: "))
       self.model = str(input("Enter Vehicle model: "))
       self.doors = int(input("Enter number of Doors: "))
       self.roof = str(input("Enter type of roof: "))
       automobile.displayInfo(self)
       
   def displayInfo(self):
        print('----------------------------------')
        print('Vehicle type: {}\nYear: {}\nMake: {}\nModel: {}\n# doors: {}\nType of roof: {}'
              .format(self.vehicleType,str(self.year),self.make,self.model,str(self.doors),self.roof))
 
       
        


if __name__ == '__main__':

    
    
    start2 = automobile()
    