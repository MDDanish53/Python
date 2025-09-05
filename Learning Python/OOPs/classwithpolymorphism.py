#polymorphism with classes method overriding

#method overriding - child class's methods override its parent class's method 

#parent class
class Bird():
    def sound(self):
        print("Birds make sound")

#child of Bird()
class Crow(Bird):
    def sound(self):
        print("Crow says Caw Caw")

#child of Bird()
class Parrot(Bird):
    def sound(self):
        print("parrot says hindi")

#creating objects
bird1 = Crow()
bird2 = Parrot()

bird1.sound() #Crow says Caw Caw
bird2.sound() #parrot says hindi

#here the method names of parent class and child class are same so the method of child class is more prior than the method of parent class, so the method of child class will execute
#both bird object have different sounds because their sound is based on the class on which the object is created 
#here there is polymorphism - sound method has different print statements based on their class, method name is same but acts differently according to the classes 
