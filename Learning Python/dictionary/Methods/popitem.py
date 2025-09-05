'''
it removes the last pair of dictionary

syntax - dict_name.popitem()

this method will return the last pair of dictionary
'''

profile = {
    "Name": "Mohammad Danish",
    "Age": 21,
    "City": "Ballarpur"
}

#removing the last pair
popped_item = profile.popitem()
print(popped_item)
print(profile)