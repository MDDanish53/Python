'''
write and read mode (w+) is used to read and write a fle. it creates a new file if not exists and overwrites the data if file exists
'''

with open(r'C:\Users\hp\OneDrive\Desktop\Learning Python\File Handling\data4'
'.txt', "w+") as file:
    content = file.read() 
    print(f'existing data = {content}')
    updated_content = input("Enter the new data = ")
    file.write(updated_content)
    print("Updated Successfully!")

#it deletes the existing data of a existing file 
#it creates new file and adds data if it not exists
#it writes the data if file exists 