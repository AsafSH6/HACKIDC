from rest_framework import viewsets
from rest_framework_extensions import mixins
from gymmy_app.models import TrainingPlan
from gymmy_app.serializers.training_plan_serializer import TrainingPlanSerializer


class TrainingPlanViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = TrainingPlan.objects.all()
    serializer_class = TrainingPlanSerializer
