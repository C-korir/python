import datetime

class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = datetime.date.today()

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        return amount

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Current balance: ${self.balance}")


if __name__ == "__main__":
    account = BankAccount("123456789", "John Doe")

    # Perform deposit
    deposit_amount = 1000
    print(f"Depositing ${deposit_amount}...")
    deposit_result = account.deposit(deposit_amount)
    print(f"Deposit successful. Amount deposited: ${deposit_amount}")

    # Perform withdrawal
    withdraw_amount = 500
    print(f"Withdrawing ${withdraw_amount}...")
    try:
        withdraw_result = account.withdraw(withdraw_amount)
        print(f"Withdrawal successful. Amount withdrawn: ${withdraw_amount}")
    except ValueError as e:
        print(e)

    # Display account information
    print("\nAccount Information:")
    account.customer_details()
    account.check_balance()