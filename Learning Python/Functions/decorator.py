'''
decorator - creating or adding a function inside main function without changing the main function's code

decorator is a function which takes another function and add it into main function without modifying the main function 

decorator is used to add functionality in a function without manipulating the function 

syntax to use a decorator - @decorator_name
'''

#creating a decorator
def my_decorator(func):
    #creating another function
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function call")
    return wrapper

#using the decorator
@my_decorator
def say_hello():
    print("hello")

#calling the decorator
say_hello()