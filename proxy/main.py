from .library import Library
from .ebook_proxy import EbookProxy
from .real_ebook import RealEbook
from .logging_ebook_proxy import LoggingEbookProxy

if __name__ == "__main__":
    library = Library()
    file_names = ["a", "b", "c"]

    for file_name in file_names:
        library.add(LoggingEbookProxy(file_name))

    library.open_ebook("a")
    library.open_ebook("b")
