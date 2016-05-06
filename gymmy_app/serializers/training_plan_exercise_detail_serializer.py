from rest_framework import serializers
from gymmy_app.models import TrainingPlanExerciseDetail


class TrainingPlanExerciseDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainingPlanExerciseDetail
