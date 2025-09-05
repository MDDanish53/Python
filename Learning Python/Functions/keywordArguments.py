'''
keyword arguments are used to provide arguments to the parameter irrespective of their order by providing the name of parameter with its value in the function call  

syntax - func_name(parameter = value, parameter = value, ...)
'''

def greet(name, city): #order - name, city
    print(city,'welcomes you',name)

greet(city="Ballarpur", name="Danish") #order - city, name