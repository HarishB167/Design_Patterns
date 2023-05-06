from typing import List
from .stock import Stock
from .observer import Observer


class StatusBar(Observer):
    __stocks: List[Stock] = []

    def add_stock(self, stock: Stock) -> None:
        self.__stocks.append(stock)
        stock.add_observer(self)

    def show(self) -> None:
        for stock in self.__stocks:
            print(stock)

    def update(self):
        print("Updating status bar")
        self.show()
