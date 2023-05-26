from .product import Product
from .real_product import RealProduct

class ProxyProduct(Product):

    def __init__(self, id: int, db_context: "DbContext") -> None:
        self._id: int = id
        self.real_product: RealProduct = RealProduct(id)
        self.db_context = db_context

    def get_id(self) -> int:
        return self.real_product.get_id()

    def get_name(self) -> str:
        return self.real_product.get_name()

    def set_name(self, name: str):
        self.real_product.set_name(name)
        self.db_context.mark_as_changed(self.real_product)
        