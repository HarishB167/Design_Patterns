from .editor import Editor
from .history import History

def main():
    editor = Editor()
    history = History()

    editor.setContent("a")
    history.push(editor.createState())

    editor.setContent("b")
    history.push(editor.createState())

    editor.setContent("c")
    editor.restore(history.pop())
    editor.restore(history.pop())

    print(editor.getContent())

if __name__ == "__main__":
    main()