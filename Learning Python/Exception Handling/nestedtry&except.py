try:
    num1 = int(input("Enter first number = ")) #if non-int data is passed by user then ValueError occurs
    num2 = int(input("Enter second number = "))

    try:
        result = num1 / num2 #if one of the value is zero then ZeroDivisionError occurs
        print(f"the result is =",result)
    except ZeroDivisionError:
        print("You cannot divide a number with zero")

except ValueError:
    print("Please enter a valid input")