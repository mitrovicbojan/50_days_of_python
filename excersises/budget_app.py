import math
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
    def __str__(self):
        title = f"{self.name:*^30}\n"
        all_transanctions = ""
        
        for transaction in self.ledger:
            all_transanctions += (
                    f"{transaction['description'][0:23]:<23}"
                    f"{transaction['amount']:>7.2f}\n"
                )
        total = f"Total: {self.get_balance()}"
        return title + all_transanctions + total    
    
def create_spend_chart(categories):
    total_spent = 0
    category_spent = []
    category_percentage = []
    category_name = []
    for category in categories:        
        for transaction in category.ledger:            
            if transaction['amount'] < 0:
                total_spent += abs(transaction['amount'])
               
    for category in categories:  
        category_sum = 0              
        for transaction in category.ledger:  
                      
            if transaction['amount'] < 0:
                category_sum  += abs(transaction['amount'])
        category_spent.append(category_sum)
        
    for num in category_spent:
        cat_percente = math.floor((num / total_spent) * 100 / 10) *10
        category_percentage.append(cat_percente)
    
    for category in categories:
        category_name.append(category.name)
    
    max_name_length = max(len(i) for i in category_name)
    
 
    print("Percentage spent by category")
    
    
    for num in range(100, -1, -10):
        row = f"{num:>3}|"
        for percentage in category_percentage:
            if num <= percentage:
                row += (" o ")
            else:
                row +="   "
        print(row)
        
    count_names = len(category_name)
    dash = "    " + "-" * (3 * count_names + 1)
   