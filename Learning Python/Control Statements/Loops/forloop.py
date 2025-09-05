'''
use for loop when we want to iterate on a sequence(list, tuple, dictionary, string)
for ex - a = [1, 2, 3]
for loop will iterate 3 times as sequence has 3 values

syntax -
for variable in sequence
    code to be executed
'''

a = [1, 2, "Mohammad Danish", 4, 5]
for i in a:
    '''
    i = variable
    a = sequence
    i will access all the elements of a one by one and iterates the loop
    i = 1 then it prints i
    i = 2 then it prints i
    i = 3 then it prints i 
    it will do the same till the last element of sequence
    we are accessing all the data of a sequence one by one using for loop and i stores the accessed data and i's value will change as we iterate the further data values
    '''
    print(i)