from .plan_factory import PlanFactory
from .workout_plan import WorkoutPlan
from .meal_plan import MealPlan
from .weight_loss_workout import WeightLossWorkout
from .weight_loss_meal_plan import WeightLossMealPlan

class WeightLossPlanFactory(PlanFactory):
    def create_workout_plan(self) -> WorkoutPlan:
        return WeightLossWorkout()

    def create_meal_plan(self) -> MealPlan:
        return WeightLossMealPlan()
        