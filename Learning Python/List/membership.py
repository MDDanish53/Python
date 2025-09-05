"""
it checks if a given element is present in the list or not
two types - in, not in
syntax - 
"""

#use of in membership 
'''
list = [1, 2, 3, 4, 5]
check = int(input("Enter a value you want to check = "))
if check in list:
    print(f'{check} is in the list')
else:
    print(f'{check} is not in the list')
'''

#use of not in membership
list = [1, 2, 3, 4, 5, 6]
input = int(input("Enter number you think it is not in the list = "))
if input not in list:
    print("Yes it is not in the list")
else:
    print("It is in the list")