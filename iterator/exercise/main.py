from .product_collection import ProductCollection
from .product import Product

if __name__ == "__main__":
    collection = ProductCollection()
    collection.push(Product(1, "Cup"))
    collection.push(Product(2, "Bowl"))
    collection.push(Product(3, "Spoon"))

    iterator = collection.createIterator()
    while iterator.hasNext():
        product = iterator.current()
        print(product)
        iterator.next()