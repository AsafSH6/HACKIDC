from rest_framework import viewsets
from rest_framework_extensions import mixins
from gymmy_app.models import Trainee
from gymmy_app.serializers.trainee_serializer import TraineeSerializer


class TraineeViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer
