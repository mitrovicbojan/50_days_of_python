class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description=""):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description=""):
        if amount < self.ledger.amount:
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            return True
        else: 
            return False

    def get_balance(self):
        return self.ledger.amount
    
    def transfer(self):
        pass
    
    def check_funds(self, amount):
        if amount > self.ledger.balance:
            return False
        return True
def create_spend_chart(categories):
    pass