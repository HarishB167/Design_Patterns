from .home_page import HomePage
from .weight_loss_plan_factory import WeightLossPlanFactory
from .build_muscle_plan_factory import BuildMusclePlanFactory

def show():
    homepage = HomePage()
    homepage.set_goal(BuildMusclePlanFactory())

if __name__ == "__main__":
    show()
