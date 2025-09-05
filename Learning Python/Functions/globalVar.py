"""
global variables are created outside the function and its scope is global and can be accessed anywhere in the program, we can access it inside any function
"""

def msg():
    #accessing global variable inside the function
    print("I like to challenge",coding)

#creating a global variable
coding = "My competitors"

msg()