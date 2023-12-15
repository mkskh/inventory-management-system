class InventoryManager():
    
    def __init__(self):
        self.inventory = []
    
    def add_product(self, product):
        self.inventory.append(product)
        return True
    
    def remove_product(self, product_name):
        for prod in self.inventory:
            if prod == product_name:
                self.inventory.remove(product_name)
                return True
    
    def update_quantities(self, product_name, new_quantity):
        for prod in self.inventory:
            if prod == product_name:
                prod.quantity = new_quantity
                # print(prod.quantity) - check for unittest
                return True
    
    def get_info(self, product_name):
        if len(self.inventory) == 0:
            print('Inventory is empty')
        else:
            for prod in self.inventory:
                if prod == product_name:
                    print(product_name.get_product_info())
                    return True
            print('Product not found')
            return False
    
    def get_total_inventory_value(self):
        total_value = 0
        for prod in self.inventory:
            total_value += prod.quantity * prod.price
        if total_value > 0:
            print(total_value)
            return True
        else:
            print('Inventory is empty')
            return False
    
    def search_product(self, product_name):
        for prod in self.inventory:
            if prod.name == product_name:
                print(f'Item with name "{product_name}" exists in your inventory. Quantity - {prod.quantity}. Price - {prod.price}.')
                return True
            
    def generate_report(self):
        if len(self.inventory) == 0:
            print('Inventory is empty')
        else:    
            total_quantity = 0
            total_price = 0
            items_list = [] # for unittest
            print('List of products in your inventory:')
            for prod in self.inventory:
                total_quantity += prod.quantity
                total_price += prod.price * prod.quantity
                items_list.append(f'- "{prod.name}". {prod.quantity} items.') # for unittest
                print(f'- "{prod.name}". {prod.quantity} items.')
            print('\nTotal quantity of items in your inventory:', total_quantity)
            print(f'Total price of all items in your inventory: ${total_price}')
            if total_quantity > 0 and len(items_list) > 0 and total_price > 0:
                return True

    def generate_statistic(self):
        if len(self.inventory) == 0:
            print('Inventory is empty')
        else:
            total_quantity = 0
            total_price = 0
            for prod in self.inventory:
                total_quantity += prod.quantity
                total_price += prod.price * prod.quantity
            average_price = total_price // total_quantity
            print(f'Average price of all items: {average_price}')
            if average_price > 0:
                return True