from rest_framework import serializers
from gymmy_app.models import Gym


class GymSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gym
