class Student():
    #self helps to store the object specific data
    def set_details(self, name, age): 
        self.name = name #stored Danish as name in object student1
        self.age = age #stored 21 as age in object student1

student1 = Student()
student1.set_details("Danish", 21) #python knows that it has to store student1 object specific name and age
print(student1.name)

#always use self, also in cases where no parameters are defined

"""
1. always use self to store properties inside an object
2. Python automatically passes the object as a self, so define self in method definition
3. without self no variables will be stored in object causing error
"""