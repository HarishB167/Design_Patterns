

class CellFormat:
    
    def __init__(self, font_family: str, font_size: int, is_bold: bool) -> None:
        self.font_family = font_family
        self.font_size = font_size
        self._is_bold = is_bold
    
    def get_font_family(self) -> str:
        return self.font_family

    def get_font_size(self) -> int:
        return self.font_size
        
    def is_bold(self) -> bool:
        return self._is_bold

    def __hash__(self) -> int:
        return hash((self.font_family, self.font_size, self._is_bold))