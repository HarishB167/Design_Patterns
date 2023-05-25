from flyweight.exercise.cell_format_factory import CellFormatFactory
from .spreadsheet import SpreadSheet

if __name__ == "__main__":
    sheet = SpreadSheet(CellFormatFactory())
    sheet.set_content(0, 0, "Hello")
    sheet.set_content(1, 0, "World")
    sheet.set_font_family(0, 0, "Arial")
    sheet.render()
