try:
    user_input = int(input("Enter a number = "))
    result = 10 / user_input
    print(f'result',result)

except ZeroDivisionError:
    print('You cannot divide a number with 0')

except ValueError:
    print('You cannot divide a number with a string')