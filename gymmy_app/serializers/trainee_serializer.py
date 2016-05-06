from rest_framework import serializers
from gymmy_app.models import Trainee


class TraineeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainee
