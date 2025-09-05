def check_password(password):
    if len(password) < 8:
        #raising custom exception 
        raise Exception("Error: Password must be >= 8 characters")
    print("Password is strong")

try:
    password = input("Enter a password = ")
    check_password(password)

#if exception is raised then except block will execute
except Exception as e: #e is short name of exception
    print(e)