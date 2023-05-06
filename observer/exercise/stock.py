from .subject import Subject


class Stock(Subject):
    __symbol: str = ""
    __price: float = 0

    def __init__(self, symbol: str, price: float) -> None:
        self.__symbol = symbol
        self.__price = price

    def get_price(self) -> float:
        return self.__price

    def set_price(self, price: float):
        self.__price = price
        self.notify_observers()
    
    def __str__(self) -> str:
        return ("Stock{" +
                "symbol='" + self.__symbol + '\'' +
                ", price=" + str(self.__price) +
                '}')