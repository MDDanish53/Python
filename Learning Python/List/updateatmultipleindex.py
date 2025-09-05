'''
it updates multiple index values using slicing
syntax - list[start_index:end_index] = new_value1, new_value2, ...(give number of values according to the start and end index-1 number values as end index is excluded)
'''

list = [1, 2, 3, 4, 5, 6, 7]
list[0: 3] = 12, 43, 13
print(list)
