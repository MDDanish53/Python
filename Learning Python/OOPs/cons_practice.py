class Student:
    #self returns object properties to the object itself
    #constructor gives different outputs for different objects
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

#creating objects
student1 = Student("Danish", 21, "C-") 
#student1 uses the same method i.e constructor
student2 = Student("Sagar", 20, "A")

print(student1.name, student1.age, student1.grade)
print(student2.name, student2.age, student2.grade)