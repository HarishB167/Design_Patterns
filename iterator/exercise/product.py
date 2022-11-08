
class Product:
  __id = 0
  __name = ""

  def __init__(self, id, name):
    self.__id = id
    self.__name = name

  def __str__(self):
    return "Product{" +"id=" + str(self.__id) + \
        ", name='" + self.__name + '\'' + '}'
