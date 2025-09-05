"""
if we want to delete a pair from a dictionary then follow:

del dict_name[key_name_to_be_deleted]

"""

my_dict = {
    "Name": "Mohammad Danish",
    "Age": 21,
    "City": "Ballarpur"
}

print(my_dict)

#deleting the Age pair
del my_dict["Age"]

print(my_dict)