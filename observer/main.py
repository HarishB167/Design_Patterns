from .data_source import DataSource
from .spreadsheet import Spreadsheet
from .chart import Chart


if __name__ == "__main__":
    data_source = DataSource()
    sheet1 = Spreadsheet(data_source)
    sheet2 = Spreadsheet(data_source)
    chart = Chart(data_source)

    data_source.add_observer(sheet1)
    data_source.add_observer(sheet2)
    data_source.add_observer(chart)

    data_source.set_value(1)