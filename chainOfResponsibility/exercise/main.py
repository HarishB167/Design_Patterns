from .excel_reader import ExcelReader
from .numbers_reader import NumbersReader
from .quick_books import QuickBooks
from .data_reader import DataReader
from .file import File

if __name__ == "__main__":

    quickbooks_reader = QuickBooks(None)
    numbers_reader = NumbersReader(quickbooks_reader)
    excel_reader = ExcelReader(numbers_reader)
    data_reader = DataReader(excel_reader)

    data_reader.handle(File("some.xls"))