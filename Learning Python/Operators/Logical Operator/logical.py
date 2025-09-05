'''
combine multiple conditions
gives a boolean value as a result

AND - all conditions must be true
OR - at least one condition must be true
NOT - operates on single operand and negates the condition

age = 20
is_student = True

print(age>18 and is_student)
print(age>25 or is_student)
print(not is_student)
'''

a = 10
b = 20

print(a>5 and b>10)
print(a<1 or b == 20)
print(not(a==10))