from .meal_plan import MealPlan
from .workout_plan import WorkoutPlan
from .plan_factory import PlanFactory

class HomePage:
    __workout_plan: WorkoutPlan = None
    __meal_plan: MealPlan = None

    def set_goal(self, factory: PlanFactory):
        self.__workout_plan = factory.create_workout_plan()
        self.__meal_plan = factory.create_meal_plan()
        print(self.__workout_plan)
        print(self.__meal_plan)
        