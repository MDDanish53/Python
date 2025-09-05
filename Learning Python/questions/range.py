start = int(input("Enter the first number = "))
stop = (int(input("Enter the last number = "))) + 1
step = int(input("Enter the step count = "))
skip = int(input("Enter the number you want to skip = "))

if start >= stop:
    print("Invalid input start")
else:
    for num in range(start, stop, step):
        if num == skip:
            continue
        elif skip > stop or skip < start:
            print("Invalid skip number")
        print(f'{num}')