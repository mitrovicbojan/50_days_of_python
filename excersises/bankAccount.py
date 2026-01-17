'''
Bank Account with Interest

Create a BankAccount class:

Instance attributes: owner (str), balance (float, default 0), interest_rate (float, default 0.01).

Methods:

deposit(amount) → adds to balance.

withdraw(amount) → subtracts from balance if enough funds, else returns "Insufficient funds".

add_interest() → increases balance by balance * interest_rate.

__str__() → returns "Owner: <owner>, Balance: <balance>".
'''

class BankAccount:
    def __init__(self, owner, balance=0, interest_rate=0.01):
                 
        self.owner= owner
        self.balance = float(balance)
        self.interest_rate = interest_rate
        
    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Please enter amount you wish to deposit.")
        else: 
            self.balance += amount
    
    def withdraw(self,amount):
        if self.balance < amount:
            return False
        self.balance -= amount
        return True
        
    def add_interest(self):
        self.balance = round(self.balance + (self.balance * self.interest_rate), 2)
        
    
    def __str__(self):        
        return f"Owner: {self.owner}, Balance: {self.balance}"