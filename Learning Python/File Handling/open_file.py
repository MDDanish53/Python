'''
inorder to work with a file inorder to read, modify, delete its data we need to open that file first using function open()

syntax - open("file_name_with_extension", "mode")

file_name = name of the file we want to open
mode = the operation(read, write, append, delete) we want to perfrom with the file
'''

#creating a object and opening File.txt file with reading operation
file = open(r'C:\Users\hp\OneDrive\Desktop\Learning Python\File Handling\File.txt', 'r') #add r before the path

#reading the file inorder to store its data
content = file.read() #content of File.txt is stored in content

print(content)

#if we open a file chances of data loss are more, so we have to close it after performing operations on it as :
file.close() #now our file's data is safe