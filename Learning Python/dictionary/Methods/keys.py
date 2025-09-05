"""
If we want to retrieve the keys of object then follow :

keys = dict_name.keys()

this will return a tuple containing list of keys, we can convert it into list 

list(keys)

""" 

profile = {
    "Name": "Mohammad Danish",
    "Age": 21,
    "Position": "Developer"
}

#retrieving the keys 
keys = profile.keys() #returns a tuple 

print(keys)

#converting tuple to list
print(list(keys))