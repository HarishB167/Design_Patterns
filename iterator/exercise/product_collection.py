from .product import Product

class ProductCollection:
    __products = []

    def push(self, product: Product):
        self.__products.append(product)

    def pop(self):
        return self.__products.pop()

    def createIterator(self):

        class ListIterator:
            def __init__(self, history: ProductCollection):
                self.__history = history
                self.__index = 0

            def hasNext(self):
                return (self.__index < len(self.__history._ProductCollection__products))

            def current(self):
                return self.__history._ProductCollection__products[self.__index]

            def next(self):
                self.__index += 1

        return ListIterator(self)