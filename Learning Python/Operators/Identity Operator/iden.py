'''
used to compare memory location of two objects(here we are not comparing data value)
two types of identity operators: 
is - returns true if memory location of two objects is same
is not - returns true if memory location of two objects is not same
'''

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
