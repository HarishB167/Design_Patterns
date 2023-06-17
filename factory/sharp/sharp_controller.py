from ..matcha.view_engine import ViewEngine
from ..matcha.controller import Controller
from .sharp_view_engine import SharpViewEngine

class SharpController(Controller):

    def create_view_engine(self) -> ViewEngine:
        return SharpViewEngine()
        