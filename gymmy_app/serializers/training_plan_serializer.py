from rest_framework import serializers
from gymmy_app.models import TrainingPlan


class TrainingPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainingPlan
