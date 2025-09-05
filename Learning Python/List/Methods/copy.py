'''
it is used to copy a variable's data in order to perform operations on the copied data without manipulationg the actual original data from where we had copied it
syntax - new_var = var_to_be_copied.copy()
'''

list = [1, 2, 3, 4, 5]
copied_list = list.copy() #copied data of list in copied_list
copied_list.insert(0, "Mohammad Danish") #manipulated data of copied_list
print(list) #data of list is as it is 
print(copied_list) #data of copied_list is changed 