from datetime import datetime

class BankAccount:
    def _init_(self, account_number, customer_name, opening_date):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = 0
        self.opening_date = opening_date if opening_date else datetime.now.today()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount {amount} deposited successfully.")
        else:
            print("Invalid amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully.")
        else:
            print("Invalid amount. Please enter a positive number less than or equal to your balance.")

    def check_balance(self):
        print(f"Your current balance is {self.balance}.")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
        print(f"Date of Opening: {self.opening_date}")
depo=float(input("Enter amount"))
win=float(input("Enter the amount"))
bal=(depo-win)
print(f"Current balance:{depo.get_balance()}")