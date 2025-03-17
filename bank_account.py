
# Bank Account Management Using OOP

class BankAccount:
    total_accounts = 0
    
    def __init__(self, account_holder, initial_balance=0):
        if not account_holder or not self.validate_amount(initial_balance):
            raise ValueError("Invalid account details.")
        self.account_holder, self.balance, self.transactions = account_holder, initial_balance, []
        BankAccount.total_accounts += 1
        print(f"Account created for {account_holder}. Total: {BankAccount.total_accounts}")
    
    def deposit(self, amount):
        if self.validate_amount(amount):
            self.balance += amount
            self.transactions.append(f"Deposited ₹{amount}")
    
    def withdraw(self, amount):
        fee = 10
        if self.validate_amount(amount) and self.balance >= amount + fee:
            self.balance -= (amount + fee)
            self.transactions.append(f"Withdrew ₹{amount} (Fee ₹{fee})")
    
    def transfer(self, recipient, amount):
        if isinstance(recipient, BankAccount) and self.validate_amount(amount):
            self.withdraw(amount)
            recipient.deposit(amount)
            self.transactions.append(f"Transferred ₹{amount} to {recipient.account_holder}")
    
    def check_balance(self):
        print(f"{self.account_holder}'s balance: ₹{self.balance}")
    
    def get_transaction_history(self):
        return self.transactions
    
    @classmethod
    def total_bank_accounts(cls):
        return cls.total_accounts
    
    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and 0 < amount <= 50000

class SavingsAccount(BankAccount):
    interest_rate, min_balance = 0.05, 500
    
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            super().withdraw(amount)
    
    def apply_interest(self):
        self.deposit(self.balance * self.interest_rate)

class CurrentAccount(BankAccount):
    overdraft_limit = 10000
    
    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            super().withdraw(amount)


savings, current = SavingsAccount("Sohel Shaikh", 1000), CurrentAccount("Mr.Anonymous", 500)
savings.deposit(5000)
savings.withdraw(300)
savings.apply_interest()
current.withdraw(600)
current.transfer(savings, 200)
print("Sohel's Transactions:", savings.get_transaction_history())
