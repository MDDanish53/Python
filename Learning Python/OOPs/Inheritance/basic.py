#parent class
class Animal():
    def speak(self):
        print("Animals make sounds")

#child class inherits the parent class
class Dog(Animal):
    def bark(self):
        print("Dogs bark")

#creating object of child class
dog = Dog()
#accessing method of parent class in the object of child class
dog.speak()
dog.bark()