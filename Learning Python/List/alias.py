'''
alias - two variables pointing the same data
when we change one of the variables value then both variable's value will bwe changed as both are pointing the same data
if we want to change only a varaibles value without affecting value of others, for this we use copy method and we can clone it 
'''

list_1 = [1, 3, 2]
list_2 = list_1
list_2[1] = "Mahevish Sheikh"
print(list_2, list_1)