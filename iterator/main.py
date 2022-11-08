
from .browse_history import BrowseHistory

if __name__ == "__main__":
    history = BrowseHistory()
    history.push("a")
    history.push("b")
    history.push("c")

    iterator = history.createIterator()
    while iterator.hasNext():
        url = iterator.current()
        print(url)
        iterator.next()