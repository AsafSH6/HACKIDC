from rest_framework import viewsets
from rest_framework_extensions import mixins
from gymmy_app.models import TrainingPlanExerciseDetail
from gymmy_app.serializers.training_plan_exercise_detail_serializer import TrainingPlanExerciseDetailSerializer


class TrainingPlanExerciseDetailViewSet(viewsets.ModelViewSet, mixins.NestedViewSetMixin):

    queryset = TrainingPlanExerciseDetail.objects.all()
    serializer_class = TrainingPlanExerciseDetailSerializer
