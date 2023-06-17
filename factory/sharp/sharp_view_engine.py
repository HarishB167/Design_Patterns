from ..matcha.view_engine import ViewEngine

class SharpViewEngine(ViewEngine):

    def render(self, viewName: str, context: dict) -> str:
        return "View rendered by Sharp"
        