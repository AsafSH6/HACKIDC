from rest_framework_extensions.routers import ExtendedDefaultRouter
from gymmy_app import viewsets

router = ExtendedDefaultRouter()
(
    router.register(r'trainees', viewsets.TraineeViewSet, base_name='trainees')
        .register(r'personal-progresses', viewsets.PersonalProgressViewSet, base_name='trainee-personal-progress',
                  parents_query_lookups=['trainee']),

    router.register(r'gyms', viewsets.GymViewSet, base_name='gyms'),

    router.register(r'exercises', viewsets.ExerciseViewSet, base_name='exercises'),

    router.register(r'gym-machines', viewsets.GymMachineViewSet, base_name='gym-machines'),

    router.register(r'training-planes', viewsets.TrainingPlanViewSet, base_name='training-planes'),

    router.register(r'personal-progresses', viewsets.PersonalProgressViewSet, base_name='personal-progresses'),

    router.register(r'training-plan-exercise-details', viewsets.TrainingPlanExerciseDetailViewSet,
                    base_name='training-plan-exercise-details'),

    router.register(r'training-plan-exercise-progresses', viewsets.TrainingPlanExerciseDetailViewSet,
                    base_name='training-plan-exercise-progresse'),
)

urlpatterns = router.urls
