'''
Parameter - parameter are varaibles which act as a placeholder for the values which will pass inside the function at the time of function call. Parameter is passed while function creation.

Argument - arguments are the values which we pass while calling a function
'''

def greet(name): #parameter - name
    print('Hello', name)

greet("Danish") #Argument - "Danish"
greet("Mahevish")
greet("Raman")

#Here, we had created a function once and we are using it in multiple ways using parameter and arguments

#if we create a parameter and we did not pass the argument value at the function call then error occurs

greet() #no argument value passed

'''
Types of arguments :
1. positional (the one we used in above function)
2. keyword
3. default
'''