'''
it is used to provide default values to the parameters at the time of function creation. these default values will be used when the value for parameter is not provided at the time of function call

syntax - 
def func_name(parameter="default_value", ..):
    print(paramter)

func_name()

output - default_value
'''

#creating function with default values name="Ashok" and city="Chandrapur"
def greet(name="Ashok", city="Chandrapur"):
    print(city,'welcomes you',name)

greet()