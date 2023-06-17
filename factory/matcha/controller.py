from .view_engine import ViewEngine
from .matcha_view_engine import MatchaViewEngine

class Controller:

    def render(self, viewName: str, context: dict) -> None:
        engine = self.create_view_engine()
        html = engine.render(viewName, context)
        print(html)

    def create_view_engine(self) -> ViewEngine:
        return MatchaViewEngine()
        