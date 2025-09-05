'''
creates copy of variable, through which its value can be copied in another varaible
syntax - new_var = var_to_be_copied.copy()
'''

list_1 = [1, 2, 3]
list_2 = list_1.copy() #creating copy of list_1
list_2[0] = "Mohammad" #modifying copied data
print(list_1, list_2) #copied one changed, original is as it is