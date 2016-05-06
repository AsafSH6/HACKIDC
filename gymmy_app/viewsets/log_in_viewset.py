from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class LogInApiView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.pop('username')
        password = request.data.pop('password')
        try:
            user = User.objects.get(username=username)
            if user.check_password(password) is True:
                return Response(request.user.trainees.first().pk, status=status.HTTP_200_OK)
            else:
                return Response(False, status=status.HTTP_401_UNAUTHORIZED)
        except ObjectDoesNotExist as e:
            return Response(False, status=status.HTTP_401_UNAUTHORIZED)
