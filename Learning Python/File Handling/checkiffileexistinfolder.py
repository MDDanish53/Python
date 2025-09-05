"""
if we are working with a file then it is a good practice to check if it exists or not

syntax - 

import os 

if os.path.exists("file_name or location"):
    print("Exists")
else:
    print("Not Exists)
"""

import os

if os.path.exists(r'C:\Users\hp\OneDrive\Desktop\Learning Python\File Handling\data10.txt'):
    print("Exists")
else:
    print("Not Exists")