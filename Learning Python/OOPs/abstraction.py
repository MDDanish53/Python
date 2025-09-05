'''
hiding complex implementation details from user and show the details which are necessary for the user.

to implement it we have to use abstract classes and methods

Ex - while driving a car we use brakes, accelarator, gears we don't need to know how these things works internally, their working is hided

to use abstract class - 

we need to import abstract class as - 

from abc import ABC, abstractmethod (to implement abstract class we need to use abstract classes and methods)

and pass ABC in the class definition as - 
class class_name(ABC):

and write the abstractmethod as - 
class class_name(ABC):
    @abstractmethod //to tell that it is a abstract method
'''

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass #no code implemented

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button")

car = Car()
bike = Bike()

car.start()
bike.start()

"""
1. Abstraction hides unnecessary details and reduces the complexity of structure through which user can use it easily
2. Abstract classes can be instantiated instead they act as a blueprint
3. child classes must define abstract classes
"""