'''
1. return is used to exit from a function and go to where it was called.
2. we can return any value from a function and that value will be found where the function is called
3. if we want to get the return value of function then we have to store the function call in a variable

when we use return statement in a function and call that function, then we have to store that function call in a variable in order to get the returned value , as the returned value is stored in the function call

return sends a value to the caller and exits the function
print displays information 
'''

def info(name, surname):
    '''return the full_name in a neat format'''
    full_name = f'{name} {surname}' #storing name and surname
    return full_name #returning full_name

store_name = info("Danish", "Siddique") #has full_name value
print(store_name)
