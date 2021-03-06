from rest_framework import viewsets
from rest_framework_extensions import mixins
from gymmy_app.models import GymMachine
from gymmy_app.serializers.gym_machine_serializer import GymMachineSerializer


class GymMachineViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = GymMachine.objects.all()
    serializer_class = GymMachineSerializer
