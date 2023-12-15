import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from inventory.inventory_manager import InventoryManager
from inventory.product import Product


# python3 -m unittest -v
# python3 test_inventory_manager.py
class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        self.inventory_manager = InventoryManager()

    def test_add_product(self):
        test_apple = Product('Apple', 700, 12)
        result = self.inventory_manager.add_product(test_apple)
        self.assertTrue(result) 

# python3 -m unittest -v test_inventory_manager.TestInventoryManager.test_add_product
    
    def test_remove_product(self):
        test_hp = Product('Hp Laptop', 1200, 8)
        result_add = self.inventory_manager.add_product(test_hp)
        self.assertTrue(result_add) 
        result_del = self.inventory_manager.remove_product(test_hp)
        self.assertTrue(result_del)

# python3 -m unittest -v test_inventory_manager.TestInventoryManager.test_remove_product

    def test_update_quantities(self):
        test_lg = Product('LG TV', 700, 16)
        result_add = self.inventory_manager.add_product(test_lg)
        self.assertTrue(result_add) 
        result_upd = self.inventory_manager.update_quantities(test_lg, 11)
        self.assertTrue(result_upd)

# python3 -m unittest -v test_inventory_manager.TestInventoryManager.test_update_quantities

    def test_get_info(self):
            test_lenovo = Product('Lenovo headphones', 200, 22)
            result_add = self.inventory_manager.add_product(test_lenovo)
            self.assertTrue(result_add) 
            result_get = self.inventory_manager.get_info(test_lenovo)
            self.assertTrue(result_get)

# python3 -m unittest -v test_inventory_manager.TestInventoryManager.test_get_info
            
    def test_get_total_inventory_value(self):
            test_lenovo = Product('Lenovo headphones', 200, 22)
            test_lg = Product('LG TV', 700, 16)
            test_hp = Product('Hp Laptop', 1200, 8)
            result_add1 = self.inventory_manager.add_product(test_lenovo)
            self.assertTrue(result_add1) 
            result_add2 = self.inventory_manager.add_product(test_lg)
            self.assertTrue(result_add2) 
            result_add3 = self.inventory_manager.add_product(test_hp)
            self.assertTrue(result_add3) 
            result_total = self.inventory_manager.get_total_inventory_value()
            self.assertTrue(result_total)

# python3 -m unittest -v test_inventory_manager.TestInventoryManager.test_get_total_inventory_value
            
    def test_search_product(self):
            test_lenovo = Product('Lenovo headphones', 200, 22)
            result_add = self.inventory_manager.add_product(test_lenovo)
            self.assertTrue(result_add) 
            result_search = self.inventory_manager.search_product('Lenovo headphones')
            self.assertTrue(result_search)

    def test_generate_report(self):
            test_lenovo = Product('Lenovo headphones', 200, 22)
            result_add = self.inventory_manager.add_product(test_lenovo)
            test_lg = Product('LG TV', 700, 16)
            result_add2 = self.inventory_manager.add_product(test_lg)
            self.assertTrue(result_add2)
            self.assertTrue(result_add) 
            result_report = self.inventory_manager.generate_report()
            self.assertTrue(result_report)

    def test_generate_statistic(self):
            test_lenovo = Product('Lenovo headphones', 200, 22)
            result_add = self.inventory_manager.add_product(test_lenovo)
            test_lg = Product('LG TV', 700, 16)
            result_add2 = self.inventory_manager.add_product(test_lg)
            self.assertTrue(result_add2)
            self.assertTrue(result_add) 
            result_stat = self.inventory_manager.generate_statistic()
            self.assertTrue(result_stat)

if __name__ == '__main__':
    unittest.main()