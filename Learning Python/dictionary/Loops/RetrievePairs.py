'''
if we want to retreive the key:value pairs then follow :

for i in dict_name.items():
    print(i)

'''

profile = {
    "Name": "Mohammad Danish",
    "Age": 21,
    "City": "Ballarpur"
}

for pairs in profile.items():
    print(pairs)