from typing import List
from .cell import Cell


class SpreadSheet:
    MAX_ROWS = 3
    MAX_COLS = 3

    def __init__(self) -> None:
        self.font_family: str = "Times New Roman"
        self.font_size: int = 12
        self.is_bold: bool = False

        self.cells: List[List[Cell]] = [[None, None, None],[None, None, None],[None, None, None]]

        self.generate_cells()
        
    def set_content(self, row: int, col: int, content: str):
        self.ensure_cell_exists(row, col)
        self.cells[row][col].set_content(content)

    def set_font_family(self, row: int, col: int, font_family: str):
        self.ensure_cell_exists(row, col)
        cell = self.cells[row][col]
        self.cells[row][col].set_font_family(font_family)

    def ensure_cell_exists(self, row: int, col: int):
        if (row < 0 or row >= self.MAX_ROWS):
            raise Exception("Illegal argument")
        
        if (col < 0 or col >= self.MAX_COLS):
            raise Exception("Illegal argument")

    def generate_cells(self):
        for row in range(self.MAX_ROWS):
            for col in range(self.MAX_COLS):
                cell = Cell(row, col)
                cell.set_font_family(self.font_family)
                self.cells[row][col] = cell
                
    def render(self):
        for row in range(self.MAX_ROWS):
            for col in range(self.MAX_COLS):
                self.cells[row][col].render()

