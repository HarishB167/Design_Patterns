from .document import Document
from .history import History

if __name__ == "__main__":
    doc = Document()
    doc.setContent("New page here")
    doc.setFontName("Arial")
    doc.setFontSize(12)

    history = History()
    history.push(doc.createState())
    print(doc)

    doc.setContent("Second page here")
    doc.setFontName("Courier")
    doc.setFontSize(13)
    # history.push(doc.createState())

    print(doc)

    doc.restore(history.pop())
    print(doc)
