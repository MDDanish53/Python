'''
Exclusive creation mode with read and write (x+) - Creates a new file but fails if it exists. it does not overwrite existing data. it prints existing data
'''

with open(r'C:\Users\hp\OneDrive\Desktop\Learning Python\File Handling\data5.txt') as file:
    content = file.read()
    print(content)
    new_content = input("Enter new content = ")
    file.write(new_content) #not writable

#it prints the existing data
#it not overwrites existing data
#it does not create new file