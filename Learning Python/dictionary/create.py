#creation of dictionary
my_dict1 = {
    "Name": "Danish",
    "Age": 21,
    100: "MD"
}

#storing list as value
my_dict2 = {
    "marks": [13, 23, 67, 67],
}

#if key name are same then the previous value in the dictionary gets overwrited by new value
my_dict3 = {
    "marks": 34,
    "marks": 89,
}

print(my_dict3) #{'marks': 89}