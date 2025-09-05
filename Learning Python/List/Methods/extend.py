'''
if we have two different lists, and we want to add the elements of list_2 at the end of list_1 then we extend the list_1
syntax - list_which_we_want_to_extend.extend(list_which_we_want_to_attach)
here - list_1.extend(list_2)
'''

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_1.extend(list_2)
print(list_1)