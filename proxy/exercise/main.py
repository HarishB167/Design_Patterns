from .db_context import DbContext
from .product import Product

if __name__ == "__main__":
    db_context = DbContext()

    # We read an object (eg a product) from a database.
    product = db_context.get_product(1)

    # We modify the properties of the object in memory.
    product.set_name("Updated Name")

    # DbContext should keep track of changed objects in memory.
    # When we call saveChanges(), it'll automatically generate
    # the right SQL statements to update our database.
    db_context.save_changes()

    # After saving the changes to the database, we can
    # change our in-memory object again and save the changes.
    product.set_name("Another name")
    db_context.save_changes()


