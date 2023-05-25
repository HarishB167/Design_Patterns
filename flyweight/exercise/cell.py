from .cell_format import CellFormat

class Cell:

    def __init__(self, row: int, column: int, cell_format: CellFormat) -> None:
        self.row: int = row
        self.column: int = column
        self.cell_format :CellFormat = cell_format
        self.content: str = ""

    def get_content(self) -> str:
        return self.content

    def set_content(self, content: str):
        self.content = content

    def set_format(self, cell_format: CellFormat):
        self.cell_format = cell_format

    def get_format(self) -> CellFormat:
        return self.cell_format
    
    def render(self):
        font_family = self.cell_format.font_family
        print(f"({self.row}, {self.column}): {self.content} [{font_family}]")
