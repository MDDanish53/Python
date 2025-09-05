try:
    file = open('C:\Users\hp\OneDrive\Desktop\Learning Python\Exception Handling\error.txt', 'r')
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File not found!")

finally:
    file.close()
    print("file read successfully")