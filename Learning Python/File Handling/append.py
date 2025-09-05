'''
append mode is used to add the new data at the end of exisiting data of the file
'''

#opening a file with append operation
with open(r'C:\Users\hp\OneDrive\Desktop\Learning Python\File Handling\data2.txt', 'a') as file:
    #taking new data from user
    content = input("Enter data to be appended = ")
    #appending content in file using write function
    file.write(content)
    print("Data appended successfully!")