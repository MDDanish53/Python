"""
creating dictionary using comprehension as :

syntax - {i: expression for i in iterable}

i - key

"""

#dictionary of squares from 1-5
squares = {x: x*x for x in range(1, 6)}
print(squares)