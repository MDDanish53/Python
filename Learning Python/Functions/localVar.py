'''
local variables are created inside a function and we can use these variables inside that function only, we cannot access these variables outside the function 
'''

def msg():
    #local varaible
    text = "I will succeed"
    print(text)

msg()

#trying the access of text(local variable) outside the function
#print(text) #error(accessing local variable globally)