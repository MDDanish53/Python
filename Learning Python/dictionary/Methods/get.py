'''
this method is used to retreive a value of a specific key in a dictionary

syntax - 

dict.get(key_name, message)

here, message = when key is not found in the dictionary then this message will be displayed, if message is not defined then the output will ne None

'''

profile = {
    "Name": "Mohammad Danish",
    "Age": 21,
    "City": "Ballarpur"
}

#Getting the value of key "Age"
age = profile.get("Age", "Not Found")
print(age) #21

#Getting value of key "Class" which not exist
Class = profile.get("Class", "Not Found")
print(Class) #Not Found