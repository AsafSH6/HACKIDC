from rest_framework import viewsets
from rest_framework_extensions import mixins
from gymmy_app.models import TrainingPlanExerciseProgress
from gymmy_app.serializers.training_plan_exercise_progress_serializer import TrainingPlanExerciseProgressSerializer


class TrainingPlanExerciseProgressViewSet(viewsets.ModelViewSet, mixins.NestedViewSetMixin):

    queryset = TrainingPlanExerciseProgress.objects.all()
    serializer_class = TrainingPlanExerciseProgressSerializer
