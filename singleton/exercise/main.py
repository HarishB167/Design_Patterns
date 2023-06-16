from .logger import Logger

if __name__ == "__main__":
    logger1 = Logger.get_instance("file1");
    logger2 = Logger.get_instance("file1")
    print(logger1 == logger2)

    logger3 = Logger.get_instance("file2")
    print(logger1 == logger3)
    