from .view_engine import ViewEngine

class MatchaViewEngine(ViewEngine):

    def render(self, viewName: str, context: dict) -> str:
        return "View rendered by Matcha"

