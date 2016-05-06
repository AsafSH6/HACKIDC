from rest_framework import viewsets
from rest_framework_extensions import mixins
from gymmy_app.models import Gym
from gymmy_app.serializers.gym_serializer import GymSerializer


class GymViewSet(viewsets.ModelViewSet, mixins.NestedViewSetMixin):

    queryset = Gym.objects.all()
    serializer_class = GymSerializer
