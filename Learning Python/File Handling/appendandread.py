'''
append and read mode (a+) opens a file for reading and appending, preserving existing data, it creates a new file if not exists. it does not overwrites exisiting data.  
'''

with open(r'C:\Users\hp\OneDrive\Desktop\Learning Python\File Handling\data5.txt', 'a+') as file:
    exist = file.read()
    print(f' existing data = {exist}')
    content = input("Enter new content = ")
    file.write(content)
    print("Content added successfully!")

#it does not show existing data
#it adds new data after existing data