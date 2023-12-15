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