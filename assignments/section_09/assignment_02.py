'''
HW: Assignment Bank Account Management System OOP
Assignment Description:

The purpose of this assignment is to provide practical exposure to Python's Object-Oriented Programming (OOP) principles.
You'll create a simple bank account management system with classes, objects, attributes, and methods.

Task:

Create a BankAccount class and a Bank class.

The BankAccount class should have the following attributes: account_number, account_holder, balance. 
It should also have the following methods: deposit(), withdraw().

The Bank class should manage multiple bank accounts. 
It should have methods to add_account(), remove_account() and get_total_assets().


Requirements:

1. Use OOP principles to design and implement the BankAccount and Bank classes.

2. BankAccount should not allow withdrawal if the balance is insufficient.

3. The Bank should store multiple BankAccount instances and manage them.

4. The Bank's get_total_assets() method should return the sum of the balances of all its accounts.

Deliverables:

bank_system.py - The source code of the Python script which implements and demonstrates the BankAccount and Bank classes.

'''
class BankAccount:
    
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if(self.balance < amount):
            print(f"Insufficient balance. Current balance: {self.balance}")
        else:
            self.balance -= amount
            return amount

class Bank:
    pass