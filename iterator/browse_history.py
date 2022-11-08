from .iterator_interface import IteratorInterface

class BrowseHistory:
    __urls = []

    def push(self, url):
        self.__urls.append(url)

    def pop(self):
        return self.__urls.pop()

    def createIterator(self):

        class ListIterator(IteratorInterface):
            def __init__(self, history: BrowseHistory):
                self.__history = history
                self.__index = 0

            def hasNext(self):
                return (self.__index < len(self.__history._BrowseHistory__urls))

            def current(self):
                return self.__history._BrowseHistory__urls[self.__index]

            def next(self):
                self.__index += 1
        
        return ListIterator(self)