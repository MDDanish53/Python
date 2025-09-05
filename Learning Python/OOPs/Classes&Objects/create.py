'''
to create a class follow the syntax :

class class_name():
    //methods and properties
'''

#creating a class(blueprint)
class Car():
    #methods
    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")

#creating objects of class Car
car1 = Car() #using properties and methods of Car class
car2 = Car()

#calling methods of objects as they are created from the class 
car1.start()
car1.stop()

car2.start()
car2.stop()