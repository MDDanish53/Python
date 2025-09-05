# constructor method will execute automatically when an object is created as it is a default method
#constructor method will automatically set the values of properties as soon as we create an object 

class Car():
    #constructor(executes automatically)
    def __init__(self, brand, color):
        self.brand = brand #self.brand stores value of brand inside the object
        self.color = color

#creating object
car1 = Car("Audi", "White") #values of properties gets set automatically
#here we passed the values of properies at the time of object creation

print(car1.brand)
print(car1.color)