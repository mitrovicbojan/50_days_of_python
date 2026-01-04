titles = ['name', 'price', 'calories_per_slice', 'toppings']
val_list = ['Margherita Pizza', 8.9, 250, ['mozzarella', 'basil']]

pizza_dict = dict(zip(titles, val_list))

print(pizza_dict['name'])

pizza_dict.update({'price': 15, "total_time": 25})

print(pizza_dict.items())

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)

for index, product in enumerate(products.items()):
    print(index, product)