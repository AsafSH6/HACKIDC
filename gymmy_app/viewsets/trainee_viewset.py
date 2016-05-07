from django.http import QueryDict
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework_extensions import mixins
from rest_framework.decorators import detail_route
from rest_framework import status
from rest_framework.response import Response
from gymmy_app.models import Trainee
from gymmy_app.serializers.trainee_serializer import TraineeSerializer
from gymmy_app.serializers.training_plan_exercise_detail_serializer import TrainingPlanExerciseDetailSerializer


class TraineeViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

    def create(self, request, *args, **kwargs):

        if isinstance(request.data, QueryDict):
            return super(TraineeViewSet, self).create(request, *args, **kwargs)
        else:
            username = request.data['email']
            password = request.data.pop('password')
            email = request.data.pop('email')
            new_user = User.objects.create_user(username=username,
                                        password=password,
                                        email=email)
            new_trainee = Trainee(user=new_user, **request.data).save()
            return Response(new_trainee.pk, status=status.HTTP_201_CREATED)

    @detail_route(methods=['GET'])
    def get_current_training_plan(self, request, *args, **kwargs):
        trainee = self.get_object()
        current_plan = trainee.training_planes.all().latest('date')
        return Response(current_plan.pk, status=status.HTTP_200_OK)

    @detail_route(methods=['GET'])
    def get_current_training_plan_exercises(self, request, *args, **kwargs):
        trainee = self.get_object()
        current_plan = trainee.training_planes.all().latest('date')
        current_plan_exercises = current_plan.exercise_details.all()
        return Response(TrainingPlanExerciseDetailSerializer(current_plan_exercises, many=True).data, status=status.HTTP_200_OK)


