"""
If we want to retrieve the values of object then follow :

values = dict_name.values()

this will return a tuple containing list of values, we can convert it into list 

list(values)

""" 

profile = {
    "Name": "Mohammad Danish",
    "Age": 21,
    "Position": "Developer"
}

#retrieving the values of dict
values = profile.values()

print(values)

print(list(values))