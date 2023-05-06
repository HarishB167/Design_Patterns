from .stock import Stock
from .status_bar import StatusBar
from .stock_list_view import StockListView


if __name__ == "__main__":
    stocks = [Stock("Apple", 25), Stock("MSN", 250), Stock("Google", 124)]

    status_bar = StatusBar()
    stock_view = StockListView()

    for stock in stocks:
        status_bar.add_stock(stock)
        stock_view.add_stock(stock)

    stocks[0].set_price(500)
    stocks[1].set_price(20)