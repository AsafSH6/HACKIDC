from rest_framework import viewsets
from rest_framework_extensions import mixins
from gymmy_app.models import Exercise
from gymmy_app.serializers.exercise_serializer import ExerciseSerializer


class ExerciseViewSet(viewsets.ModelViewSet, mixins.NestedViewSetMixin):

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
