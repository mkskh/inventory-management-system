import inventory



samsung_tv = inventory.Product('Samsung', 400, 5)

print('Test Product class methods:')
print('Name -', samsung_tv.name)
print('Price -', samsung_tv.price)
print('Quantity -', samsung_tv.quantity)
samsung_tv.update_quantity(15)
samsung_tv.update_price(405)
samsung_tv.update_name('Samsung TV Big Screen')
print('After ganges:')
samsung_tv.get_product_info()
print('')

stock = inventory.InventoryManager()

stock.add_product(samsung_tv)

hp_notebook = inventory.Product('Hp', 600, 10)
stock.add_product(hp_notebook)

apple_smartphone = inventory.Product('Apple iPhone', 1200, 19)
stock.add_product(apple_smartphone)

# stock.get_info(apple_smartphone)

print('Total inventory value')
print(stock.get_total_inventory_value())

# print(stock.inventory)
