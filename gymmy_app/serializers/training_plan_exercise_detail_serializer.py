from rest_framework import serializers
from gymmy_app.models import TrainingPlanExerciseDetail
from gymmy_app.serializers.exercise_serializer import ExerciseSerializer


class TrainingPlanExerciseDetailSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(instance='exercise', read_only=True)

    class Meta:
        model = TrainingPlanExerciseDetail
