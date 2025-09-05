'''
positional arguments are the arguments which we pass position wise based on the position of parameter

ex - if we created a parameter name in a function and then another parameter after name is city then at the time of function call we need to pass the value of name at first then the value of city after that
'''

def greet(name, city): #1. name, 2. city
    print(f'{city} welcomes you {name}')

greet("Danish", "Mumbai") #1. name value, 2.city value