'''
if we have two lists and we want to get the common elements between these two lists,
we can do this as follows: 

1. convert both the lists into sets as: set(list)
2. store both the sets into variables 
3. now apply intersection method to both the sets as: set1.intersection(set2)
4. now store the intersection in a varaible and convert that variable from set to list if you want
the final variable contains the common data value
'''

list_1 = [1, 2, 3, 4, 5]
list_2 = [3, 4, 5, 6, 7]

set_1 = set(list_1)
set_2 = set(list_2)

common = list(set_1.intersection(set_2))
print(f"common values are = {common}")