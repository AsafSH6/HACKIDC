from rest_framework import serializers
from gymmy_app.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
