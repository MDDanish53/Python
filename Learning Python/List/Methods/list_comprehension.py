'''
it is concise, powerful, readable way to create a list 

syntax - [expression for item in iterable if condition]

where,
expression - operation to be performed (x * 2)
item - element of sequence
iterable - sequence where we will apply loop (range(1, 11))
condition - any filtration if needed (optional)  
'''

#code without comprehension
'''
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)
'''

#code with comprehension
squares = [i ** 2 for i in range(1, 11) if i%2 == 0]
print(squares)