from .cell_format import CellFormat

class CellFormatFactory:

    def __init__(self) -> None:
        self.formats :dict = {}

    def get_cell_format(self, font_family: str, font_size: int, is_bold: bool) -> CellFormat:
        key = hash((font_family, font_size, is_bold))
        if key not in self.formats:
            format = CellFormat(font_family, font_size, is_bold)
            self.formats[key] = format
        return self.formats[key]

