from .product import Product

class RealProduct(Product):

    def __init__(self, id: int) -> None:
        self._id: int = id
        self.name: str = ""

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name
        