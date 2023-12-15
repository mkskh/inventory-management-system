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

hp_notebook = inventory.Product('Hp notebook', 600, 10)
stock.add_product(hp_notebook)

apple_smartphone = inventory.Product('Apple iPhone', 1200, 19)
stock.add_product(apple_smartphone)

# stock.get_info(apple_smartphone)

print('Total inventory value')
stock.get_total_inventory_value()

# print(stock.inventory)

stock.search_product('Samsung TV Big Screen')
print('')

lenovo_headphones = inventory.Product('Lenovo headphones', 200, 22)
lg_tv = inventory.Product('LG TV', 700, 16)
hp_lap = inventory.Product('Hp Laptop', 1200, 8)
stock.add_product(lenovo_headphones)
stock.add_product(lg_tv)
stock.add_product(hp_lap)

stock.generate_report()

print('')

stock.generate_statistic()