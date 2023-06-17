from .home_page import HomePage
from .goal import Goal

def show():
    homepage = HomePage()
    homepage.set_goal(Goal.STRENGTH_TRAINING)

if __name__ == "__main__":
    show()
