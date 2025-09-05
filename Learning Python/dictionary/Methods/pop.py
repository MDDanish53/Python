'''
this method is used to remove a pair from the dictionary

syntax - dict_name.pop(key_name_to_be_popped, message_if_key_not_exist)

this method will return the value of the popped_key
'''

profile = {
    "Name": "Danish",
    "Age": 21,
    "City": "Ballarpur"
}

popped = profile.pop("Age", "Not Found")
print(popped) #21

print(profile)