from .group import Group
from .shape import Shape

if __name__ == "__main__":
    group1 = Group()
    group1.add(Shape())
    group1.add(Shape())

    group2 = Group()
    group2.add(Shape())
    group2.add(Shape())

    group = Group()
    group.add(group1)
    group.add(group2)
    group.render()
    group.move()

