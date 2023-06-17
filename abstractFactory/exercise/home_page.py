from .workout_plan import WorkoutPlan
from .meal_plan import MealPlan
from .goal import Goal
from .build_muscle_workout import BuildMuscleWorkout
from .build_muscle_meal_plan import BuildMuscleMealPlan
from .weight_loss_workout import WeightLossWorkout
from .weight_loss_meal_plan import WeightLossMealPlan

class HomePage:
    __workout_plan: WorkoutPlan = None
    __meal_plan: MealPlan = None

    def set_goal(self, goal: Goal):
        if goal == Goal.BUILD_MUSCLE:
            self.__workout_plan = BuildMuscleWorkout()
            self.__meal_plan = BuildMuscleMealPlan()
        elif goal == Goal.WEIGHT_LOSS:
            self.__workout_plan = WeightLossWorkout()
            self.__meal_plan = WeightLossMealPlan()
        print(self.__workout_plan)
        print(self.__meal_plan)
        