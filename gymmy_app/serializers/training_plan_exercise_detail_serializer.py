from rest_framework import serializers
from gymmy_app.models import TrainingPlanExerciseDetail
from gymmy_app.serializers.exercise_serializer import ExerciseSerializer


class TrainingPlanExerciseDetailSerializer(serializers.ModelSerializer):
    exercise_instance = ExerciseSerializer(source='exercise', read_only=True)

    class Meta:
        model = TrainingPlanExerciseDetail
        fields = ('id', 'training_plan', 'exercise', 'exercise_instance', 'breaks_between_exercises', 'trainer_notes', 'trainee_notes')
        extra_kwargs = {'exercise': {'write_only': True}}
