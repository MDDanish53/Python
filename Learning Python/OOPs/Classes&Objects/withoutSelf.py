class Student():
    def set_details(name, age):
        name = name #it does not do anything as no value is stored inside the object
        age = age

student1 = Student()
student1.set_details("Danish", 21) #python does not know given name & age belongs to student1 object
print(student1.name) #attribute error