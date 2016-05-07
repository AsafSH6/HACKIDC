from rest_framework import serializers
from gymmy_app.models import Exercise
from gymmy_app.serializers.gym_machine_serializer import GymMachineSerializer


class ExerciseSerializer(serializers.ModelSerializer):
    gym_machine_instance = GymMachineSerializer(source='gym_machine', read_only=True)

    class Meta:
        model = Exercise
        fields = ('id', 'name', 'gym_machine', 'gym_machine_instance', 'muscle', 'level', 'description', 'video_url')
        extra_kwargs = {'gym_machine': {'write_only': True}}

