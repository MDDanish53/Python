'''
generator generates a single value at a time on our demand, it uses very less memory
generator function behaves like an iterator 

for ex - we use for loop to generate numbers from 1 to 10 using range, it will give us all the numbers 
but if we need only one number then we can get it throught generator, the memory is consumed only for one number .
in generator we have to use "yield" keyword
'''

#yield keyowrd
def count_down(num):
    while num > 0:
        yield num #yield one value at a time
        num -= 1

for i in count_down(5):
    print(i) 

#generators are used to evaluate data lazily

#if we want only 5 then it will give 5
#after 5 then it will give 4 and then 3 and yield will remember the order
#it will give one value at a time 