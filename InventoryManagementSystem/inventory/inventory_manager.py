class InventoryManager():
    
    def __init__(self):
        self.inventory = []
    
    def add_product(self, product):
        self.inventory.append(product)
    
    def remove_product(self, product_name):
        for prod in self.inventory:
            if prod == product_name:
                self.inventory.remove(product_name)
    
    def update_quantities(self, product_name, new_quantity):
        for prod in self.inventory:
            if prod == product_name:
                prod.quantity = new_quantity
    
    def get_info(self, product_name):
        if len(self.inventory) == 0:
            print('Inventory is empty')
        else:
            for prod in self.inventory:
                if prod == product_name:
                    return product_name.get_product_info()
            print('Product not found')
    
    def get_total_inventory_value(self):
        total_value = 0
        for prod in self.inventory:
            total_value += prod.quantity * prod.price
        return total_value