from .product import Product
from .proxy_product import ProxyProduct

class DbContext:

    def __init__(self) -> None:
        self.updated_objects = {}
        
    def get_product(self, id) -> Product:
        # Automatically generate SQL statements
        # to read the product with the given ID.
        print(f"SELECT * FROM products WHERE product_id = {id}")

        # Simulate reading a product object from a database.
        product = ProxyProduct(id, self)
        product.set_name("Product 1")

        return product
        
    def save_changes(self):
        # Automatically generate SQL statements
        # to update the database.
        for key in self.updated_objects:
            updated_object: Product = self.updated_objects[key]
            print(f"UPDATE products SET name = '{updated_object.get_name()}' WHERE product_id = {updated_object.get_id()}")

        self.updated_objects = {}

    def mark_as_changed(self, product: Product):
        self.updated_objects[product.get_id()] = product
