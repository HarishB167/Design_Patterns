from .matcha.controller import Controller
from .sharp.sharp_controller import SharpController

class ProductsController(SharpController):

    def listProducts(self ):
        # Get products from a database
        context = {}
        # context.put(products)
        self.render("products.html", context)
