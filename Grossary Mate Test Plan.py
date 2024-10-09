import unittest
# Mock Data for Testing
products = [
    {"name": "Apples", "price": 1.50, "category": "Fruit"},
    {"name": "Milk", "price": 3.00, "category": "Dairy"},
    {"name": "Bread", "price": 2.50, "category": "Bakery"},
]
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, product):
        self.items.append(product)
    def remove_item(self, product):
        if product in self.items:
            self.items.remove(product)
    def get_total(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total
class GroceryMateTests(unittest.TestCase):
    def test_user_registration(self):
        # Mock user registration logic
        user = User("testuser", "password123")
        self.assertIsNotNone(user)
    def test_login(self):
        # Mock login logic
        user = User("testuser", "password123")
        self.assertTrue(user.username == "testuser" and user.password == "password123")
    def test_search_products(self):
        # Mock product search logic
        search_term = "Milk"
        results = [product for product in products if search_term in product["name"]]
        self.assertTrue(len(results) > 0)
    def test_add_to_cart(self):
        cart = ShoppingCart()
        cart.add_item(products[0])
        self.assertEqual(len(cart.items), 1)
    def test_remove_from_cart(self):
        cart = ShoppingCart()
        cart.add_item(products[0])
        cart.remove_item(products[0])
        self.assertEqual(len(cart.items), 0)
    def test_get_total(self):
        cart = ShoppingCart()
        cart.add_item(products[0])
        cart.add_item(products[1])
        self.assertEqual(cart.get_total(), 4.50)
if __name__ == '__main__':
    unittest.main()