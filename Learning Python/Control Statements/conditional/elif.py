age = int(input("Enter your age = "))

if age >= 101:
    print("You are dead brother")
elif age >= 18:
    print("You can vote")
elif age <= 0:
    print("You are a ghost")
else:
    print("You cannot vote")