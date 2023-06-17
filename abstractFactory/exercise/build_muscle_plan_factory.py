from .plan_factory import PlanFactory
from .workout_plan import WorkoutPlan
from .meal_plan import MealPlan
from .build_muscle_workout import BuildMuscleWorkout
from .build_muscle_meal_plan import BuildMuscleMealPlan

class BuildMusclePlanFactory(PlanFactory):
    def create_workout_plan(self) -> WorkoutPlan:
        return BuildMuscleWorkout()

    def create_meal_plan(self) -> MealPlan:
        return BuildMuscleMealPlan()
        