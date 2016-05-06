from rest_framework import serializers
from gymmy_app.models import PersonalProgress


class PersonalProgressSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalProgress
