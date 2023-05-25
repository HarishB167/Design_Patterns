from typing import List

from .cell_format import CellFormat
from .cell_format_factory import CellFormatFactory
from .cell import Cell


class SpreadSheet:
    MAX_ROWS = 3
    MAX_COLS = 3

    def __init__(self, cell_format_factory: CellFormatFactory) -> None:
        self.format_fact: CellFormatFactory = cell_format_factory

        self.cells: List[List[Cell]] = [[None, None, None],[None, None, None],[None, None, None]]

        self.generate_cells()
        
    def set_content(self, row: int, col: int, content: str):
        self.ensure_cell_exists(row, col)
        self.cells[row][col].set_content(content)

    def set_font_family(self, row: int, col: int, font_family: str):
        self.ensure_cell_exists(row, col)
        cell = self.cells[row][col]
        old_format = cell.get_format()
        format_obj = self.format_fact.get_cell_format(font_family, old_format.font_size, old_format.is_bold())
        cell.set_format(format_obj)

    def ensure_cell_exists(self, row: int, col: int):
        if (row < 0 or row >= self.MAX_ROWS):
            raise Exception("Illegal argument")
        
        if (col < 0 or col >= self.MAX_COLS):
            raise Exception("Illegal argument")

    def generate_cells(self):
        for row in range(self.MAX_ROWS):
            for col in range(self.MAX_COLS):
                cell = Cell(row, col, self.get_default_format())
                self.cells[row][col] = cell

    def get_default_format(self) -> CellFormat:
        return self.format_fact.get_cell_format("Times New Roman", 12, False)
                
    def render(self):
        for row in range(self.MAX_ROWS):
            for col in range(self.MAX_COLS):
                self.cells[row][col].render()

