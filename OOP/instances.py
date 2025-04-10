class BankAccount:
    bank_name = "hdfc"
    interest_rate = 0.04  # class variables

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner} deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"Interest of ₹{interest:.2f} applied. New balance: ₹{self.balance:.2f}")

    @classmethod
    def set_interest_rate(cls, new_rate):
        if 0 <= new_rate <= 0.1:
            cls.interest_rate = new_rate
            print(f"New interest rate set to: {cls.interest_rate * 100}%")
        else:
            print("Interest rate should be between 0% and 10%")
    @staticmethod
    def validate_account_number(account_number):
        return str(account_number).isdigit() and len(str(account_number)) == 10

account1 = BankAccount("vikram")
# print(account1.validate_account_number(1234567890))   #static method
# print(BankAccount.validate_account_number(1234567890))  #static method

print(account1.interest_rate)

print("before changing interest_rate...")
BankAccount.set_interest_rate(0.06)
# account1.set_interest_rate(0.06)

# print(account1.interest_rate)


print("Interst rate after altering using class method")
account2 = BankAccount("Mainul")
print(account2.interest_rate)