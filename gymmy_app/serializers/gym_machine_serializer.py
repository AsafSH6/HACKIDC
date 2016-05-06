from rest_framework import serializers
from gymmy_app.models import GymMachine


class GymMachineSerializer(serializers.ModelSerializer):

    class Meta:
        model = GymMachine
