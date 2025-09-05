"""
polymorphism - one name, many forms
through polymorphism we can use same method or operator on different objects to behave differently
means same function name will work for different data types 
means same method name will work differently for different classes   

Ex - run has different meanings based on usage 
1. person runs fast
2. car runs on petrol
3. computer program runs smoothly
"""

#len() works differently for different data types
print(len("Danish"))
print(len((1, 2, 3)))
print(len({"name": "Danish", "isPass": True}))
