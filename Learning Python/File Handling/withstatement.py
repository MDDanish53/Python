'''
with statement closes a file automatically after using it
'''

#opening a file with write operation using with statement
with open(r'C:\Users\hp\OneDrive\Desktop\Learning Python\File Handling\data.txt', 'w') as file:
    #writing the opened file with user input data
    content = input("Enter new data = ")
    file.write(content)
    print("Saved")
    

#this file will automatically close after writing operation
