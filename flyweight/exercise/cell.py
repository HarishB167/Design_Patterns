
class Cell:

    def __init__(self, row: int, column: int) -> None:
        self.row: int = row
        self.column: int = column
        self.content: str = ""
        self.font_family: str = ""
        self.font_size: int = 0
        self._is_bold: bool = False

    def get_content(self) -> str:
        return self.content

    def set_content(self, content: str):
        self.content = content
    
    def get_font_family(self) -> str:
        return self.font_family

    def set_font_family(self, font_family: str):
        self.font_family = font_family

    def get_font_size(self) -> int:
        return self.font_size

    def set_font_size(self, font_size: int):
        self.font_size = font_size
        
    def is_bold(self) -> bool:
        return self._is_bold

    def set_is_bold(self, bold: bool):
        self._is_bold = bold

    def render(self):
        print(f"({self.row}, {self.column}): {self.content} [{self.font_family}]")
