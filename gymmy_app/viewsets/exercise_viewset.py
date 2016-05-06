from rest_framework import viewsets
from rest_framework_extensions import mixins
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import status
from gymmy_app.models import Exercise
from gymmy_app.serializers.exercise_serializer import ExerciseSerializer


class ExerciseViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    @detail_route(methods=['GET'])
    def get_replacement(self, request, *args, **kwargs):
        exercise = self.get_object()
        replacement_exercises = Exercise.objects.filter(muscle=exercise.muscle, level=exercise.level).exclude(id=exercise.pk)
        if replacement_exercises is not None:
            return Response(ExerciseSerializer(replacement_exercises, many=True).data, status=status.HTTP_200_OK)
        else:
            return Response('error', status=status.HTTP_404_NOT_FOUND)


