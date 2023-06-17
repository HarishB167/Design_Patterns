from .workout_plan import WorkoutPlan
from .meal_plan import MealPlan

class PlanFactory:

    def create_workout_plan(self) -> WorkoutPlan:
        pass

    def create_meal_plan(self) -> MealPlan:
        pass