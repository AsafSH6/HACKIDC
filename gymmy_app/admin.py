from django.contrib import admin
from gymmy_app.models import *

admin.site.register(Trainee)
admin.site.register(Gym)
admin.site.register(GymMachine)
admin.site.register(Exercise)
admin.site.register(TrainingPlan)
admin.site.register(TrainingPlanExerciseDetail)
admin.site.register(TrainingPlanExerciseProgress)
admin.site.register(PersonalProgress)