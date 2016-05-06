from rest_framework_extensions.routers import ExtendedDefaultRouter
from gymmy_app import viewsets


router = ExtendedDefaultRouter()

trainees = router.register(r'trainees', viewsets.TraineeViewSet, base_name='trainees')
trainees.register(r'personal-progresses', viewsets.PersonalProgressViewSet, base_name='trainee-personal-progress', parents_query_lookups=['trainee'])
trainees.register(r'training-plans', viewsets.TrainingPlanViewSet, base_name='trainee-training-plans', parents_query_lookups=['trainee'])

router.register(r'gyms', viewsets.GymViewSet, base_name='gyms')

router.register(r'exercises', viewsets.ExerciseViewSet, base_name='exercises')

router.register(r'gym-machines', viewsets.GymMachineViewSet, base_name='gym-machines')

training_planes = router.register(r'training-plans', viewsets.TrainingPlanViewSet, base_name='training-plans')
training_planes.register('exercise-details', viewsets.TrainingPlanExerciseDetailViewSet, base_name='training-plans-exercies-details', parents_query_lookups=['training_plan'])

router.register(r'personal-progresses', viewsets.PersonalProgressViewSet, base_name='personal-progresses')

router.register(r'training-plan-exercise-details', viewsets.TrainingPlanExerciseDetailViewSet, base_name='training-plan-exercise-details')

router.register(r'training-plan-exercise-progresses', viewsets.TrainingPlanExerciseDetailViewSet, base_name='training-plan-exercise-progresse')


urlpatterns = router.urls

