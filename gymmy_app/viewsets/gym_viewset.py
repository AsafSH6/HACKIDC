from rest_framework import viewsets
from rest_framework_extensions import mixins
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import status
from gymmy_app.models import Gym
from gymmy_app.serializers.gym_serializer import GymSerializer
from gymmy_app.serializers.gym_machine_serializer import GymMachineSerializer


class GymViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = Gym.objects.all()
    serializer_class = GymSerializer

    @detail_route(methods=['GET'])
    def get_gym_machines(self, request, *args, **kwargs):
        gym = self.get_object()
        gym_machines = gym.gym_machines.all()
        serialized_gym_machine = GymMachineSerializer(gym_machines, many=True).data
        return Response(serialized_gym_machine, status=status.HTTP_200_OK)
