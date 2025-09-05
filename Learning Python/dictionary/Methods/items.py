"""
this method provides all the key:value pairs of a dictionary

syntax - dict_name.items()

this will return a tuple having list of key:value pairs

convert this tuple into a list 

the list will contain the tuples, each containing a key with its value

"""

profile = {
    "Name": "Danish",
    "Age": 21,
    "Position": "Developer"
}

#retrieving all the items from profile
all_items = profile.items()
print(all_items)

#converting tuple into list
print(list(all_items))

#we can retrieve values using for loop, we will discuss this in future