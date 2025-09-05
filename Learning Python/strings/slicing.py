"""
used to access a part of string

syntax - 
string[start:stop:step]
start - starting index from where we want the string(default 0)
stop - stop index + 1 as stop is excluded, to set the end(default the last index)
step - interval between characters(default 1)
"""

name = "Pythonisveryeasylanguage"
print(name[1:11:2])

#to print whole string left to right
hobby = "Playing free fire"
print(hobby[::1])

#to print string in reverse(right to left)
interest = "not interested"
print(interest[::-1])