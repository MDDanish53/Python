'''
read and write (r+) mode is used when we want to open and read a file and also we want to write the file's data. it does not create a new file.

if i read the file before the writing operation, it adds the write data at the end of file 
if i don't read the file and write the data then it adds the data at the starting of the file and deletes the existing characters to add the updated ones
'''

with open(r'C:\Users\hp\OneDrive\Desktop\Learning Python\File Handling\data2.txt', 'r+') as file:
    #reading the file's data
    content = file.read()
    print(f'existing content = {content}')
    #writing the file's data
    new_content = input("Enter the updated data = ")
    file.write(new_content)
    print("Content updated successfully!")