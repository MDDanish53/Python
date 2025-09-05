def password_strength(password):
    if len(password) < 8:
        print("Your password is too weak please enter a strong password")
        set_password()

    else:
        print("password saved successfully")

def set_password():
    password = input("Set your password = ")
    password_strength(password) 

set_password()