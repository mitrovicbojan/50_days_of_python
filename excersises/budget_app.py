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
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            return True
        else: 
            return False

    def get_balance(self):
        
        total_balance = 0
        for i in self.ledger:
            total_balance += i['amount']           
        
        return round(total_balance, 2)
            
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': f"Transfer to {category.name}",
            })
            category.ledger.append({
                'amount': amount,
                'description': f"Transfer from {self.name}",
            })
            return True
        return False
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
def create_spend_chart(categories):
    pass