class Product:
    
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
    
    def update_price(self, new_price):
        self.price = new_price
    
    def update_name(self, new_name):
        self.name = new_name

    def get_product_info(self):
        return f'Product name - {self.name}. Quantity - {self.quantity}. Price - {self.price}.'