'''
adding properties to our class
'''

class Car():
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color
    
    def show_details(self):
        print(f'The color of car is {self.color} and the brand is {self.brand}')

#creating object of class Car
car1 = Car()
car2 = Car()

#calling the set_details method of objects to set the car details
car1.set_details("Mercedes", "Black")
car2.set_details("Porsche", "Yellow")

#calling the show_details method of objects to show their setted details
car1.show_details()
car2.show_details()

"""
Here what we did:

1. we created a main logic
2. created multiple cars from the logic
3. setted properties of each car (brand, color)
4. printed those properties
"""