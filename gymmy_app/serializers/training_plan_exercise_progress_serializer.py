from rest_framework import serializers
from gymmy_app.models import TrainingPlanExerciseProgress


class TrainingPlanExerciseProgressSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainingPlanExerciseProgress
