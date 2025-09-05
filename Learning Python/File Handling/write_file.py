'''
write mode is used to overwrite the existing data of a file with new data

syntax - file_name.write(new_data)
'''

#opening a file with write operation
file = open(r'C:\Users\hp\OneDrive\Desktop\Learning Python\File Handling\sample_data1.txt', 'w')

#taking new data from user
content = input("Enter new content = ")

#writing new content in file
file.write(content)
print("Data saved successfully...")

#closing the file
file.close()