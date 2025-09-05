'''
lambda functions are anonymous functions which are defined using a single line 
to define these function we use lambda keyword
these functions does not have any name
here we dont use def keyword to define the lambda function instead we use lambda
lambda function returns the value of expression

syntax - lambda parameter:single_expression condition

while using lambda function we can send only one expression
'''

#creating a lambda function
add_ten = lambda x:x+10 
print(add_ten(4))

#generating a list
gen_seq = lambda x:list(range(1, x+1))
user_input = int(input("Enter the last range = "))
print(f'here is your list = ',gen_seq(user_input))

#lambda function reduces readability