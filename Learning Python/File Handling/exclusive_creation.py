'''
exclusive creation mode creates a file if it not exists, but it fails if the file exists. it does not overwrites the file data
'''

with open(r'C:\Users\hp\OneDrive\Desktop\Learning Python\File Handling\data3.txt', 'x') as file:
    content = input("Enter data you want in your file = ")
    file.write(content)
    print("Data saved successfully")

    #it gives error if the file exists and creates the file and adds the data if the file is not created