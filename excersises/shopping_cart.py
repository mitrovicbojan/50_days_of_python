'''
Shopping Cart

Create a ShoppingCart class:

Attributes: owner (str), items (list of dictionaries: {"name": str, "price": float}).

Methods:

add_item(name, price) → adds item dict to cart.

remove_item(name) → removes first matching item.

total() → returns total price of items.

__str__() → prints items in format: "Item: <name>, Price: <price>" and total.
'''

class ShoppingCart:
    def __init__(self, owner, items):
        self.owner = owner
        self.items = items
    
    def add_item(self,name, price):
        self.items.append({
            "name": name,
            "price": price
        })
    
    def remove_item(self, name):
        for item in self.items:
            if item['name'] == name:
                self.items.remove(item)
                break
    
    def total(self):
        cart_prices = []
        for item in self.items:
            cart_prices.append(item['price'])
            
        cart_total = sum(cart_prices)    
        return cart_total
        
    def __str__(self):
        total = f"Total: {self.total()}"
        total_bill = ""
        for item in self.items:
            total_bill += f"Item: {item['name']}, Price: {item['price']}\n"
            
        return total_bill + total