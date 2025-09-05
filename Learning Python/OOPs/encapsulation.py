'''
Encapsulation - it means hiding internal details of object, and it prohibits direct access, we cannot modify data accidentally because internal details are hided. 
we can gives control access using methods - getter() and setter()

Ex - in mobile phones, internal components (battery, circuit) are hidden(encapsulated) we have the permission to use the phone through buttons and screen only

in short, hiding sensitive data and providing only a controlled access

1. Encapsulation hides private details of class
2. class's private attributes cannot be accessed directly 
''' 

class BankAccount():
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance #private variable
    
    def deposit(self, dep_amount):
        self.__balance += dep_amount
        print(f'your current balance = {self.__balance}')

    def withdraw(self, wd_amount):
        self.__balance -= wd_amount
        print(f'your current balance is = {self.__balance}')

    def check_balance(self):
        print(f'your current balance is = {self.__balance}') #controlled access

customer1 = BankAccount("1342", 6500)

customer1.deposit(420)
customer1.withdraw(1000)
customer1.check_balance()

#trying to get the balance directly
print(customer1.__balance) #error(private varaible cannot be accessed publically)

#here, when we tried to access the __balance property then it says AttributeError: 'BankAccount' object has no attribute '__balance' as we had created it as a private variable(accessed only inside the class)