num1 = float(input("Enter first number = "))
num2 = float(input("Enter second number = "))
operator = input("Enter operator(+, -, *, /, %, //, **) = ")

if operator == "+":
    print(f"The sum is = {num1 + num2}")
elif operator == "-":
    print(f"The difference is = {num1 - num2}")
elif operator == "*":
    print(f"The multiplication is = {num1 * num2}")
elif operator == "/":
    print(f"The division is = {num1 / num2}")
elif operator == "%":
    print(f"The modulus is = {num1 % num2}")
elif operator == "//":
    print(f"The floor division is = {num1 // num2}")
elif operator == "**":
    print(f"The {num1} to the power {num2} is = {num1 ** num2}")
else:
    print("Invalid operation")

