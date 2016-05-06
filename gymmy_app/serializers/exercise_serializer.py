from rest_framework import serializers
from gymmy_app.models import Exercise
from gymmy_app.serializers.gym_machine_serializer import GymMachineSerializer


class ExerciseSerializer(serializers.ModelSerializer):
    gym_machine = GymMachineSerializer(instance='gym_machine', read_only=True)

    class Meta:
        model = Exercise
