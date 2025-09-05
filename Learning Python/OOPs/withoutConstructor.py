"""
Constructor is a special method in a class when a object is created
Constructor is used setup the initialization of object properties, doing this we can use the properties of a class inside it.

Constructor is used to initialize an object when it is created

representation - __init__()

why we need constructor ?

without constructor we need to manually call a method and have to assign the values of object's properties. Constructor automates this process
"""

#creating class without constructor
class Car():
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color

#creating object of class
car1 = Car()
#manually assigning values for object properties
car1.set_details("Audi", "Gray")
print(car1.brand)
print(car1.color)

"""
problems faced without constructor :
1. we have to manually call set_details method and assign values to properties when i made car1 object
2. if we forget to call set_details then the object will not have the idea about what to do inside the class
"""