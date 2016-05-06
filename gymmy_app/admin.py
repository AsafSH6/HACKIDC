from django.contrib import admin
from gymmy_app.models import *

admin.register(Trainee)
admin.register(Gym)
admin.register(GymMachine)
admin.register(Exercise)
admin.register(TrainingPlan)
admin.register(TrainingPlanExerciseDetail)
admin.register(TrainingPlanExerciseProgress)
admin.register(PersonalProgress)